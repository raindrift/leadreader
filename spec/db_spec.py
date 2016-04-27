from expects import *
from leadreader.db import Db

with description('Db singleton'):
    with it('always returns the same db instance'):
        db1 = Db('test').conn
        db2 = Db('test').conn
        expect(id(db1)).to(equal(id(db2)))

    with it('is a working db instance'):
        db = Db('test').conn
        db.compositions.insert_one({'filename': 'foo'})
        record = db.compositions.find_one({'filename': 'foo'})
        expect(record['filename']).to(equal('foo'))
