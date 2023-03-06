#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 09 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        for line in str.splitlines():
            yield int(line)
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield int(line)

def IsValidSum(val, box):
    for v1 in box:
        for v2 in box:
            if val == v1+v2:
                return True
    return False


BOX_SIZE = 25
lines = IterateLines()
box = [next(lines) for i in range(BOX_SIZE)]
while True:
    try:
        val = next(lines)
        if IsValidSum(val, box):
            box.pop(0)
            box.append(val)
        else:
            print( val )
            break
    except StopIteration:
        break

# -> 507622668
