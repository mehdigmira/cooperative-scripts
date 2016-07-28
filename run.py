# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

import argparse
import imp
from time import sleep


def run_remote(data=None):
    try:
        func = imp.load_source('contained', args.file_path).run()
        func.next()
        while True:
            data = func.send(data)
            func.next()
    except StopIteration:
        return StopIteration
    except KeyboardInterrupt:
        return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='run cooperative code')
    parser.add_argument('file_path', metavar='file_path', type=str, help='file to run')
    args = parser.parse_args()
    data = None
    while True:
        data = run_remote(data)
        if data is StopIteration:
            print 'byebye'
            break
        else:
            print 'You have 2s to Keyboard interrupt the program for real. Otherwise, it will be reloaded and resumed'
            try:
                sleep(2)
            except KeyboardInterrupt:
                print 'byebye'
                break




