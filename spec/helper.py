from leadreader.db import Db

def setup(self):
    self.db = Db('test').conn
    self.db.compositions.drop()
