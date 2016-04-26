from pymongo import MongoClient
from expects import *
from leadreader.composition import Composition
from leadreader.db import Db

with description('Composition'):
    with before.each:
        self.db = Db('test').conn
        self.db.compositions.drop()

    with it('creates an entry for the leadsheet in the db'):
        composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        record = self.db.compositions.find_one()

        # pending
        # expect(record.filename).to(equal('test-1-in-c-major'))
