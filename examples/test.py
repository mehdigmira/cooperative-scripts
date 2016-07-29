# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from time import sleep

data_init = range(20)


def run():
    while True:
        data = (yield)  # get data from storage

        if data is None:  # first run, initialize
            data = data_init

        if not data:  # break condition
            break

        # Logic goes here
        time_sleep = 2
        print data.pop()
        print 'sleeping %ss' % time_sleep
        sleep(time_sleep)
        ###

        yield data  # save data
