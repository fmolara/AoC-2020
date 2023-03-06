#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 25 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """5764801
17807724"""
    else:
        str = """10212254
12577395
"""
    for line in str.splitlines():
        yield line


def ParseKeys():
    for line in IterateLines():
        yield int(line)


def Transform( sjno, loopsz ):
    res = 1
    for i in range(loopsz):
        res *= sjno
        res %= 20201227
    return res


def GuessLoopSize( final_key ):
    res = 1
    for i in range(10**100):
        res *= 7
        res %= 20201227
        if res == final_key:
            return i+1
    return None


keys = tuple( [(key, GuessLoopSize( key )) for key in ParseKeys()] )
for i in range(len(keys)):
    print( keys[i] )
    print( Transform( keys[i][0], keys[(i+1)%len(keys)][1] ) )

# right -> 290487