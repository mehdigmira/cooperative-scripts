# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

import argparse
import imp


def import_function(path):
    contained_module = imp.load_source('contained', path)
    contained_module.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='run cooperative code')
    parser.add_argument('file_path', metavar='file_path', type=str, help='file to run')
    args = parser.parse_args()
    import_function(args.file_path)

