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
    contained_module = imp.load_source('contained', args.file_path)
    func = contained_module.run()
    func.next()
    x = None
    while True:
        # saved_stuff = func.next()
        # func.next()
        x = func.send(x)
        func.next()
        print x
        # func.next()
        # print saved_stuff


