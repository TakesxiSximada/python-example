# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(allow_abbrev=False)  # https://bugs.python.org/issue14910
parser.add_argument('--send', action='store_true')
args = parser.parse_args(['--se'])
print(args.send)
