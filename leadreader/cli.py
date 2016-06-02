import sys,os,argparse
from leadreader.composition import Composition

def main(args=None):
    args = parse_args(args or sys.argv[1:])

    def fetch_composition(filename):
        try:
            return Composition(filename)
        except ValueError:
            return None

    def find_leadsheets(paths, depth=0):
        sheets = []
        for path in paths:
            for root, subdirs, files in os.walk(path):
                files = [relpath for relpath in files if relpath[-4:] == '.xml']
                sheets = sheets + [os.path.join(root, relpath) for relpath in files]

        return sheets

    if args.recursive:
        sheets = find_leadsheets(args.sheets)
    else:
        sheets = args.sheets

    if sheets:
        compositions = [_f for _f in map(fetch_composition, sheets) if _f]
        for composition in compositions:
            if args.analyses:
                for analysis in args.analyses:
                    composition.analyze(analysis)
                    print("Running", analysis, 'for', composition.filename)

def parse_args(args):
    arg_parser = argparse.ArgumentParser(description='Analyze leadsheets')
    arg_parser.add_argument('-s', '--sheets', nargs='+', help='Leadsheet files to analyze')
    arg_parser.add_argument('-a', '--analyses', nargs='+', help='Analyses to run on leadsheets')
    arg_parser.add_argument('-r', '--recursive', action='store_const', const=True, help='Recursively search directories')
    return arg_parser.parse_args(args)
