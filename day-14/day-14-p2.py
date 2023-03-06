#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 14 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy
import math



def IterateLines():
    if 0:
        str = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
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
                , s_line[1]
        elif s_line[0].index('mem[') == 0:
            yield 'mem'  \
                , int( s_line[0][4:-1] ) \
                , int( s_line[1] )
        else:
            assert False, line


def ApplyMask( val, msk ):
    assert len(val) == len(msk)
    res = ''
    for v, m in zip(val, msk):
        if m == '0':
            res += v
        else:
            assert m in ('1', 'X')
            res += m
    return res


def IterFloating( val ):
    i = val.find('X')
    if i < 0:
        yield val
    else:
        for bit in "01":
            for v in IterFloating( val[:i]+bit+val[i+1:] ):
                yield v


mem = {}
msk = '0'*36
for instr in ParseInput():
    print( instr )
    if instr[0] == 'mask':
        msk = instr[1]
    elif instr[0] == 'mem':
        addr = instr[1]
        val =  instr[2]
        res =  ApplyMask( "{:036b}".format(addr), msk )
        for v in IterFloating( res ):
            mem[int(v, 2)] = val
    else:
        assert False, instr

print( sum(val for key, val in mem.items()) )
