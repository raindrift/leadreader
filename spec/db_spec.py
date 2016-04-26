from expects import *
from leadreader.db import Db

with description('Db singleton'):
    with it('always returns the same db instance'):
        db1 = Db('test').conn
        db2 = Db('test').conn
        expect(id(db1)).to(equal(id(db2)))

