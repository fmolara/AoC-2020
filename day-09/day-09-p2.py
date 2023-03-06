#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 09 / Part 2
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

def FindGuess(guess, box):
    for i, ival in enumerate(box):
        acc = ival
        for j, jval in enumerate(box[i+1:]):
            acc += jval
            if acc == guess:
                #print i,     ival )
                #print( j+i+1, jval )
                return i, j+i+1
    return None

# p1 -> 507622668
GUESS = 507622668
box = [val for val in IterateLines()]
i, j = FindGuess(GUESS, box)
res = min(box[i:j+1]) \
    + max(box[i:j+1])
print(res)
