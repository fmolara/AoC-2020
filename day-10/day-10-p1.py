#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 10 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
#import numpy



def IterateLines():
    if 0:
        str = """16
10
15
5
1
11
7
19
6
12
4"""
        for line in str.splitlines():
            yield int(line)
    elif 0:
        str = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
        for line in str.splitlines():
            yield int(line)
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield int(line)

def IterateDiffs(devices):
    prev = devices[0]
    for dev in devices[1:]:
        diff = dev-prev
        yield diff
        prev = dev

devices = sorted([line for line in IterateLines()])
print(devices)
devices.insert( 0, 0 )
devices.append( devices[-1]+3 )
print(devices)
diffs = [diff for diff in IterateDiffs(devices)]
print(diffs)
print( diffs.count(1) )
print( diffs.count(3) )
print( diffs.count(1)*diffs.count(3) )
