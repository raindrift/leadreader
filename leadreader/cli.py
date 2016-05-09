import sys,argparse
from leadreader.composition import Composition

def main(args=None):
    args = parse_args(args or sys.argv[1:])

    def fetch_compositon(filename):
        return Composition(filename)

    if args.sheets:
        compositions = map(fetch_compositon, args.sheets)
        for composition in compositions:
            if args.analyses:
                for analysis in args.analyses:
                    composition.analyze(analysis)
                    print "Running", analysis, 'for', composition.filename

def parse_args(args):
    arg_parser = argparse.ArgumentParser(description='Analyze leadsheets')
    arg_parser.add_argument('-s', '--sheets', nargs='+')
    arg_parser.add_argument('-a', '--analyses', nargs='+')
    return arg_parser.parse_args(args)
