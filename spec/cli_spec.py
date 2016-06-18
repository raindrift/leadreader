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

        with it('takes a list of analyses'):
            args = cli.parse_args(['-a', 'foo', 'bar'])
            expect(args.analyses).to(equal(['foo', 'bar']))

    with description('list analyses'):
        with it('obtains list of available analyses'): 
            # TODO: Should probably replace this with a fake suite of analyses, so that
            # this does not have to be updated when new analyses are
            # implemented.
            expected = {'key_manual': 'Manually input key for a composition.', 'key_sapp_simple': "Determine key using Krumhansl's algorithm and Craig Sapp's simple weights", 'key_krumhansl': "Determine key using Krumhansl's algorithm and Krumhansl-Shmuckler weighting", 'key_temperley_kostka_payne': "Determine key using Krumhansl's algorithm and Temperley-Kostka-Payne weightings", 'modulation_windows': 'Determine key modulations using sliding measure windows', 'metadata': 'Extract and store basic composition metadata', 'key_bellman_budge': "Determine key using Krumhansl's algorithm and Bellman-Budge weightings", 'key_krumhansl_kessler': "Determine key using Krumhansl's algorithm and Krumhansl-Kessler weightings", 'key_aarden_essen': "Determine key using Krumhansl's algorithm and Aarden-Essen weightings (not recommended for minor)"}
            expect(cli.get_analyses()).to(equal(expected))

    with description('main'):
        with it('lists available analyses'):
            pass

        with it('loads composition objects for all the specified sheets'):
            cli.main(['-s', 'spec/fixtures/test-1-in-c-major.xml', 'spec/fixtures/test-1-in-c-major-copy.xml'])
            record = self.db.compositions.find_one({'filename': 'test-1-in-c-major.xml'})
            expect(record['filename']).to(equal('test-1-in-c-major.xml'))
            expect(self.db.compositions.count()).to(equal(2))

        with it('runs analyses for the specified compositions'):
            cli.main(['-s', 'spec/fixtures/test-1-in-c-major.xml', '-a', 'metadata'])
            record = self.db.compositions.find_one({'filename': 'test-1-in-c-major.xml'})
            expect(record['metadata']['title']).to(equal('Test 1 in C Major'))

        with it('recursively searches directories for compositions, and skips non-leadsheets'):
            cli.main(['-r', '-s', 'spec/fixtures'])
            expect(self.db.compositions.count()).to(equal(2))
