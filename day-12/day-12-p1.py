#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 12 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """F10
N3
F7
R90
F11"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line

def IterateCommands():
    for line in IterateLines():
        yield line[0], int(line[1:])



rot_CW_90 = {
    'S': 'W',
    'N': 'E',
    'W': 'N',
    'E': 'S',
}

rot_CCW_90 = {
    'S': 'E',
    'N': 'W',
    'W': 'S',
    'E': 'N',
}

def Rotate( face, _dir, magn ):
    assert _dir in ('L', 'R')
    assert magn in (90, 180, 270)
    rot = rot_CW_90 if _dir == 'R' else rot_CCW_90
    while magn > 0:
        face = rot[face]
        magn -= 90
    return face


directions = {
    #                    X   Y
    'S': numpy.array( (  0, -1 ) ),
    'N': numpy.array( (  0, +1 ) ),
    'W': numpy.array( ( -1,  0 ) ),
    'E': numpy.array( ( +1,  0 ) ),
}

pos = numpy.array( (0, 0) )
face = 'E'
for _dir, magn in IterateCommands():
    if _dir == 'F':
        _dir = face

    if _dir in ('L', 'R'):
        face = Rotate( face, _dir, magn )
    elif _dir in directions:
        pos += magn*directions[_dir]
    else:
        assert False, _dir


print( pos )
print(abs( pos[0] )+abs( pos[1] ))

# 1956
