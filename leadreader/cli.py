import sys,os,argparse
import pkgutil
from leadreader.composition import Composition

# Entry point to the command.
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

    if args.list:
        analyses = get_analyses()
        # Aligned output.
        template = '{0:26} - {1:50}'
        print('\nAvailable analyses:\n')
        for analysis, desc in analyses.items():
            print(template.format(analysis, desc))
    
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
    arg_parser.add_argument(
      '-s', '--sheets', nargs='+', help='Leadsheet files to analyze')
    arg_parser.add_argument(
      '-a', '--analyses', nargs='+', help='Analyses to run on leadsheets')
    arg_parser.add_argument(
      '-l', '--list', action='store_const', const=True,
      help='List all available analyses with descriptions')
    arg_parser.add_argument(
      '-r', '--recursive', action='store_const', const=True,
      help='Recursively search directories')
    # Default -h if nothing provided.
    if 0 >= len(args):
        arg_parser.print_help()
    return arg_parser.parse_args(args)

# Analyses modules to ignore.
IGNORE = ['base']

# Returns a dict mapping available analyses name to their description.
def get_analyses():
    # Use absolute path from the current file so that the command works from
    # any directory.
    path = os.path.dirname(os.path.abspath(__file__)) + '/analyses'
    dict = {}
    for importer, mod, ispkg in pkgutil.iter_modules([path]):
        if mod in IGNORE or ispkg: continue
        m = importer.find_module(mod).load_module(mod)
        members = dir(m)
        # Valid members look like ['BaseAnalysis', '$AnalysisClass', ...]
        if 'BaseAnalysis' == members[0]:
            AnalysisClass = getattr(m, members[1])
            # Does not need to be a real composition analysis.
            c = AnalysisClass(None)
            # TODO: Perhaps change BaseAnalysis.description to @staticmethod,
            # although static+abstract requires a clunkier decorator.
            description = c.description()
            dict[mod] = description
    return dict


