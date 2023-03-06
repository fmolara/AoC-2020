#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 05 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import sys, numpy



def IterateLines():
    if 0:
        str = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def Str2BoardPass(line):
    bin_line = line.replace('B', '1') \
                   .replace('F', '0') \
                   .replace('R', '1') \
                   .replace('L', '0')
    row = int(bin_line[:7], base=2)
    col = int(bin_line[7:], base=2)
    return row, col


plane = numpy.zeros( (128,8), dtype=int )

for line in IterateLines():
    row, col = Str2BoardPass(line)
    plane[row, col] = 1

#numpy.set_printoptions(threshold=sys.maxsize)
#print( plane )
for r in range(128):
    print( r, plane[r, :] )
