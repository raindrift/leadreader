from expects import *
import leadreader.cli as cli

with description('Command Line'):
    with description('Argument Parsing'):
        with it('builds a list of compositions'):
            args = cli.parse_args(['-s', 'foo', 'bar'])
            expect(args.sheets).to(equal(['foo', 'bar']))
