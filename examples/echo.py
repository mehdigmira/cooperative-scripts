# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from time import sleep


def run():
    while True:
        x = (yield)  # get data from storage
        if x is None:  # first run, initialize
            x = 0
        if x > 10:
            break
        yield x + 1  # save data
        print x + 1
        sleep(2)
        print 'yo'
