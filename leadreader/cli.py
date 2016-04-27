import sys,argparse
from leadreader.composition import Composition

def main(args=None):
    args = parse_args(args or sys.argv[1:])

    def fetch_compositon(filename):
        return Composition(filename)

    if args.sheets:
        compositions = map(fetch_compositon, args.sheets)
        for composition in compositions:
            print "Processing", composition.filename

def parse_args(args):
    arg_parser = argparse.ArgumentParser(description='Analyze leadsheets')
    arg_parser.add_argument('-s', '--sheets', nargs='+')
    return arg_parser.parse_args(args)
