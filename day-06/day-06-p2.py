#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 06 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """abc

a
b
c

ab
ac

a
a
a
a

b"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def IterateGroups():
    grp = []
    for line in IterateLines():
        if line:
            grp.append( line )
        else:
            yield grp
            grp.clear()
    if line:
        yield grp


def GroupCount(grp):
    cnt = {}
    for form in grp:
        for answ in form:
            cnt[answ] = cnt[answ]+1 if answ in cnt else 1
    #print( grp, cnt )
    return sum( 1 for answ, card in cnt.items() if card == len(grp) )


#for grp in IterateGroups():
#    print( grp, GroupCount(grp) )

print( sum( [GroupCount(grp) for grp in IterateGroups()] ) )
