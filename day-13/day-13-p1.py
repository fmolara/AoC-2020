#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 13 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy
import math



def IterateLines():
    if 0:
        str = """939
7,13,x,x,59,x,31,19"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def ParseInput():
    lines = IterateLines()
    line_0 = next(lines)
    line_1 = next(lines)
    return int(line_0), \
           [int(id) for id in filter(lambda el: el != 'x', line_1.split(','))]


ts, IDs = ParseInput()
delays = [0 if ts % _id == 0 else _id - ts % _id for _id in IDs]
print( ts )
print( IDs )
print( delays )
i_min = numpy.argmin(delays)
print( "ID = ", IDs[i_min] )
print( "delays = ", delays[i_min] )
print( "res = ", IDs[i_min]*delays[i_min] )

# right -> 2305
