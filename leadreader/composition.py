import os
import importlib
from xml.dom.minidom import parse

from leadreader.db import Db
from leadreader.str import camelize

class Composition(dict):
    def __init__(self, path):
        self.db = Db().conn
        self.path = os.path.abspath(path)
        filename = os.path.basename(path)
        self.xml = False # memoize this

        if not os.path.isfile(self.path):
            raise IOError("file not found: " + self.path)

        dom = self.xmldom()
        if not dom.getElementsByTagName('score-partwise'):
            raise ValueError(self.path + " is not a leadsheet")

        self.record = self.db.compositions.find_one({'filename': filename})

        if not self.record:
            self._create_record()

        self.__initialized = True

    def __getattr__(self, attr):
        try:
            return self.record[attr]
        except KeyError:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if '_Composition__initialized' not in self.__dict__:  # this test allows attributes to be set in the __init__ method
            return dict.__setattr__(self, attr, value)
        elif attr in self.__dict__: # instance variables are maintained as-is
            dict.__setattr__(self, attr, value)
        else:
            self.__dict__['record'][attr] = value
            self.db.compositions.update_one({'_id': self.record['_id']}, {'$set': self.record})

    def __bool__(self):
        return True

    def __dir__(self):
        return dir(self.record)

    def __repr__(self):
        return repr(self.record)

    def _create_record(self):
        result = self.db.compositions.insert_one({
            'filename': os.path.basename(self.path),
            'path': self.path
        })

        self.record = self.db.compositions.find_one({'_id': result.inserted_id})

    def xmldom(self):
        if not self.xml:
            self.xml = parse(self.path)

        return self.xml

    def analyze(self, analysis_name):
        try:
            analysis_module = importlib.import_module('leadreader.analyses.' + analysis_name)
        except ImportError:
            raise AttributeError('Missing analysis: ' + analysis_name)

        analysis_class = getattr(analysis_module, camelize(analysis_name))
        analysis = analysis_class(self)
        analysis.analyze()

