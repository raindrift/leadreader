import sys,os,argparse
from leadreader.composition import Composition

def main(args=None):
    args = parse_args(args or sys.argv[1:])

    def fetch_compositon(filename):
        return Composition(filename)

    def find_leadsheets(paths, depth=0):
        sheets = []
        for path in paths:
            for root, subdirs, files in os.walk(path):
                files = filter(lambda relpath: relpath[-4:] == '.xml', files)
                sheets = sheets + map(lambda relpath: os.path.join(root, relpath), files)

        return sheets

    if args.recursive:
        sheets = find_leadsheets(args.sheets)
    else:
        sheets = args.sheets

    if sheets:
        compositions = map(fetch_compositon, sheets)
        for composition in compositions:
            if args.analyses:
                for analysis in args.analyses:
                    composition.analyze(analysis)
                    print "Running", analysis, 'for', composition.filename

def parse_args(args):
    arg_parser = argparse.ArgumentParser(description='Analyze leadsheets')
    arg_parser.add_argument('-s', '--sheets', nargs='+', help='Leadsheet files to analyze')
    arg_parser.add_argument('-a', '--analyses', nargs='+', help='Analyses to run on leadsheets')
    arg_parser.add_argument('-r', '--recursive', action='store_const', const=True, help='Recursively search directories')
    return arg_parser.parse_args(args)
