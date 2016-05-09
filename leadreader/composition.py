import os
import importlib
from xml.dom.minidom import parse

from leadreader.db import Db
from leadreader.str import camelize

class Composition(dict):
    def __init__(self, path):
        self.db = Db().conn
        path = os.path.abspath(path)
        filename = os.path.basename(path)
        if not os.path.isfile(path):
            raise IOError("file not found: " + path)
        self.record = self.db.compositions.find_one({'filename': filename})

        if not self.record:
            self._create_record(path)

        self.__initialized = True

    def __getattr__(self, attr):
        try:
            return self.record[attr]
        except KeyError:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if not self.__dict__.has_key('_Composition__initialized'):  # this test allows attributes to be set in the __init__ method
            return dict.__setattr__(self, attr, value)
        elif self.__dict__.has_key(attr): # instance variables are maintained as-is
            dict.__setattr__(self, attr, value)
        else:
            self.__dict__['record'][attr] = value
            self.db.compositions.update_one({'_id': self.record['_id']}, {'$set': self.record})


    def _create_record(self, path):
        result = self.db.compositions.insert_one({
            'filename': os.path.basename(path),
            'path': path
        })

        self.record = self.db.compositions.find_one({'_id': result.inserted_id})

    def xmldom(self):
        return parse(self.path)

    def analyze(self, analysis_name):
        try:
            analysis_module = importlib.import_module('leadreader.analyses.' + analysis_name)
        except ImportError:
            raise AttributeError('Missing analysis: ' + analysis_name)

        analysis_class = getattr(analysis_module, camelize(analysis_name))
        analysis = analysis_class(self)
        analysis.analyze()

