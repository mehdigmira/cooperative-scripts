# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division


def run():
    while True:
        x = (yield)
        if x is None:
            x = 0
        if x > 10:
            break
        yield x + 1
