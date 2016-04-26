from pymongo import MongoClient

# singleton pattern, from Bruce Eckel

class Db:
    class __Db:
        def __init__(self, dbname):
            self.val = dbname
            self.client = MongoClient('mongodb://localhost:27017/')
            self.conn = self.client['leadreader_' + dbname]

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, dbname='prod'):
        if not Db.instance:
            Db.instance = Db.__Db(dbname)
        else:
            Db.instance.val = dbname

    def __getattr__(self, name):
        return getattr(self.instance, name)
