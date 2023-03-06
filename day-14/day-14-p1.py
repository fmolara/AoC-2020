#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 14 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy
import math



def IterateLines():
    if 0:
        str = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def ParseInput():
    for line in IterateLines():
        s_line = line.split(' = ')
        if s_line[0] == 'mask':
            yield 'mask'  \
                , int( s_line[1].replace('X', '1'), 2 ) \
                , int( s_line[1].replace('X', '0'), 2 )
        elif s_line[0].index('mem[') == 0:
            yield 'mem'  \
                , int( s_line[0][4:-1] ) \
                , int( s_line[1] )
        else:
            assert False, line


mem = {}
msk_and, msk_or = 0, 0
for instr in ParseInput():
    print( instr )
    if instr[0] == 'mask':
        msk_and, msk_or = instr[1:]
        print( instr, msk_and, msk_or )
    elif instr[0] == 'mem':
        val = instr[2]
        val &= msk_and
        val |= msk_or
        print( instr, val )
        mem[instr[1]] = val
    else:
        assert False, instr

print(mem)
print( sum(val for key, val in mem.items()) )
