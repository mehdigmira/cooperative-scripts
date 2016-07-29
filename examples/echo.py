# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from time import sleep


def run():
    while True:
        data = (yield)  # get data from storage

        if data is None:  # first run, initialize
            data = 0

        if data > 10:  # break condition
            break

        # Logic goes here
        data += 1
        print 'that is ', data
        sleep(2)
        ###

        yield data  # save data
