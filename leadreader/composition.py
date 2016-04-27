import os
from leadreader.db import Db

class Composition:
    def __init__(self, path):
        self.db = Db().conn
        path = os.path.abspath(path)
        filename = os.path.basename(path)
        if not os.path.isfile(path):
            raise IOError("file not found: " + path)
        self.record = self.db.compositions.find_one({'filename': filename})

        if not self.record:
            self._create_record(path)

    def __getattr__(self, attr):
        if attr in self.record:
            return self.record[attr]
        else:
            raise AttributeError(attr)

    def _create_record(self, path):
        result = self.db.compositions.insert_one({
            'filename': os.path.basename(path),
            'path': path
        })

        self.record = self.db.compositions.find_one({'_id': result.inserted_id})

