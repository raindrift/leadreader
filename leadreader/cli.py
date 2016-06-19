"""
cli.py
Leadreader's command line interface.
"""
import sys
import os
import argparse
import pkgutil
from leadreader.composition import Composition

def main(args=None):
    """ Entry point to the leadreader command. """
    args = parse_args(args or sys.argv[1:])

    def _fetch_composition(filename):
        try:
            return Composition(filename)
        except ValueError:
            return None

    def _find_leadsheets(paths, depth=0):
        sheets = []
        for path in paths:
            for root, subdirs, files in os.walk(path):
                files = [relpath for relpath in files if relpath[-4:] == '.xml']
                sheets = sheets + [os.path.join(root, relpath)
                                   for relpath in files]

        return sheets

    if args.list:
        path = os.path.dirname(os.path.abspath(__file__)) + '/analyses'
        analyses = get_analyses(path)
        # Aligned output.
        template = '{0:26} - {1:50}'
        print('\nAvailable analyses:\n')
        for analysis, desc in analyses.items():
            print(template.format(analysis, desc))

    if args.recursive:
        sheets = _find_leadsheets(args.sheets)
    else:
        sheets = args.sheets

    if sheets:
        compositions = [_f for _f in map(_fetch_composition, sheets) if _f]
        for composition in compositions:
            if args.analyses:
                for analysis in args.analyses:
                    composition.analyze(analysis)
                    print("Running", analysis, 'for', composition.filename)

def parse_args(args):
    """ Setup all command line arguments. """
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
    if len(args) <= 0:
        arg_parser.print_help()
    return arg_parser.parse_args(args)

# Analyses modules to ignore.
IGNORE = ['base']

def _filter_members(members, name):
    if name in members:
        members.remove(name)

def get_analyses(path):
    """ Return dict mapping available analyses name to their description. """
    # Use absolute path from the current file so that the command works from
    # any directory.
    dict = {}
    for importer, mod_name, ispkg in pkgutil.iter_modules([path]):
        if mod_name in IGNORE or ispkg:
            continue
        mod = importer.find_module(mod_name).load_module(mod_name)
        members = dir(mod)
        members = list(filter(lambda n: not n.startswith('_'), members))
        _filter_members(members, 'music21')
        _filter_members(members, 'math')
        _filter_members(members, 'prompt_for_key')
        # Valid members look like ['BaseAnalysis', '$AnalysisClass', ...]
        if 'BaseAnalysis' in members:
            members.remove('BaseAnalysis')
            analysis_class = getattr(mod, members[0])
            # Does not need to be a real composition analysis.
            instance = analysis_class(None)
            # TODO: Perhaps change BaseAnalysis.description to @staticmethod,
            # although static+abstract requires a clunkier decorator.
            description = instance.description()
            dict[mod_name] = description
    return dict


