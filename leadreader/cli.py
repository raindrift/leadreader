import sys,argparse
import leadreader

def main(args=None):
    args = parse_args(args or sys.argv[1:])

def parse_args(args):
    arg_parser = argparse.ArgumentParser(description='Analyze leadsheets')
    arg_parser.add_argument('-s', '--sheets', nargs='+')
    return arg_parser.parse_args(args)
