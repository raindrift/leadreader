from expects import *
from spec.helper import *
import leadreader.cli as cli

with description('Command Line'):
    with before.each:
        setup(self)

    with description('Argument Parsing'):
        with it('builds a list of compositions'):
            args = cli.parse_args(['-s', 'foo', 'bar'])
            expect(args.sheets).to(equal(['foo', 'bar']))

    with description('main'):
        with it('loads composition objects for all the specified sheets'):
            cli.main(['-s', 'spec/fixtures/test-1-in-c-major.xml', 'spec/fixtures/test-1-in-c-major-copy.xml'])
            record = self.db.compositions.find_one({'filename': 'test-1-in-c-major.xml'})
            expect(record['filename']).to(equal('test-1-in-c-major.xml'))
            expect(self.db.compositions.count()).to(equal(2))

        with it('runs analyses for the specified compositions'):
            cli.main(['-s', 'spec/fixtures/test-1-in-c-major.xml', '-a', 'metadata'])
            record = self.db.compositions.find_one({'filename': 'test-1-in-c-major.xml'})
            expect(record['metadata']['title']).to(equal('Test 1 in C Major'))

        with it('recursively searches directories for compositions'):
            cli.main(['-r', '-s', 'spec/fixtures'])
            expect(self.db.compositions.count()).to(equal(2))
