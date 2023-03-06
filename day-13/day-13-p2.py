#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 13 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import functools
import numpy
import math



def IterateLines():
    if 0:
        #yield "7,13,x,x,59,x,31,19"
        #yield "17,x,13,19"
        yield "67,7,59,61"
        #yield "67,x,7,59,61"
        #yield "67,7,x,59,61"
        #yield "1789,37,47,1889"
    else:
        with open('input.txt') as f:
            for i, line in enumerate(f.read().splitlines()):
                if i == 0:
                    continue
                yield line


def ParseInput():
    lines = IterateLines()
    #line_0 = next(lines)
    line_1 = next(lines)
    for i, _id in enumerate(line_1.split(',')):
        if _id != 'x':
            yield int(_id), i


def lcm( *values ):
    res = 1
    for v in values:
        res = res * v // math.gcd( res, v )
    return res


def ExtGCD( a, b ):
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a//b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy


def ChineseRemainder( IDs ):
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    n = functools.reduce(lambda x, y: x*y, [_id for _id, i in IDs], 1)
    n1 = lcm(                             *[_id for _id, i in IDs] )
    print("n =   ", n)
    print("lcm = ", n1)
    res = 0
    for _id, i in IDs:
        _, r, s = ExtGCD( _id, n//_id )
        e = s * n // _id
        #print( _id, i, _id-i, e )
        res += (_id-i if i > 0 else 0)*e
    return n, res

IDs = [el for el in ParseInput()]
print( IDs )
print( [(_id, _id-i if i > 0 else 0) for _id, i in IDs] )

n, res = ChineseRemainder( IDs )
print("res =   ", res)
while res < 0:
    res += n
print("res-- = ", res)
while res-n > 0:
    res -= n
print("res++ = ", res)

## right -> 552612234243498
## wrong    49255704666894992
## too high 50703151609056511

# check
for _id, i in IDs:
    assert (res+i) % _id == 0, "Error at position {}".format(i)

