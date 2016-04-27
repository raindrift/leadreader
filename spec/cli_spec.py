from expects import *
from leadreader.db import Db
import leadreader.cli as cli

with description('Command Line'):
    with description('Argument Parsing'):
        with it('builds a list of compositions'):
            args = cli.parse_args(['-s', 'foo', 'bar'])
            expect(args.sheets).to(equal(['foo', 'bar']))

    with description('main'):
        with before.each:
            # use the test db
            self.db = Db('test').conn
            self.db.compositions.drop()

        with it('loads composition objects for all the specified sheets'):
            cli.main(['-s', 'spec/fixtures/test-1-in-c-major.xml', 'spec/fixtures/test-1-in-c-major-copy.xml'])
            record = self.db.compositions.find_one({'filename': 'test-1-in-c-major.xml'})
            expect(record['filename']).to(equal('test-1-in-c-major.xml'))
            expect(self.db.compositions.count()).to(equal(2))
