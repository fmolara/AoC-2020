#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 05 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 1:
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


def Str2SeatID(line):
    row, col = Str2BoardPass(line)
    return row*8 + col


#for line in IterateLines():
#    print( line, Str2BoardPass(line), Str2SeatID(line) )

print( max( [Str2SeatID(line) for line in IterateLines()] ) )
