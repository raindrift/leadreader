from expects import *
from spec.helper import *

with description('Db singleton'):
    with before.each:
        setup(self)

    with it('always returns the same db instance'):
        db1 = Db('test').conn
        db2 = Db('test').conn
        expect(id(db1)).to(equal(id(db2)))

    with it('is a working db instance'):
        self.db.compositions.insert_one({'filename': 'foo'})
        record = self.db.compositions.find_one({'filename': 'foo'})
        expect(record['filename']).to(equal('foo'))
