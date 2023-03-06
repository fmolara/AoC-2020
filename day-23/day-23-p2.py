#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 23 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy, math



def GetLine():
    if 0:
        return "389125467"
    else:
        return "962713854"


def IterCups():
    M = None
    for c in GetLine():
        c = int(c)
        if M is None or M < c:
            M = c
        yield c
    for c in range( M+1, 1000001 ):
        yield c


def PrintSequence( pBegin, N ):
    for i in range(N):
        print(pBegin[0], ' ', end='')
        pBegin = pBegin[1]
    print()


cups = {}
pHead, pCur = None, None
for c in IterCups():
    pNew = [c, None]
    cups[c] = pNew
    if pCur:
        pCur[1] = pNew
    else:
        pHead = pNew
    pCur = pNew
pCur[1] = pHead



TURN_COUNT = 10000000
for turn in range(TURN_COUNT):
    if turn%10000==0: print(turn/10000000*100.0)
    #print(turn, " | ", end='')
    #PrintSequence( pHead, len(cups) )

    c = pHead[0]

    # Forward 3 nodes
    pGroup, group = pHead[1], []
    pNext = pHead[1]
    for i in range(3):
        group.append( pNext[0] )
        pNext = pNext[1]

    # Short-circuit pHead to end of pGroup
    pHead[1] = pNext

    # find destination cup
    dest_c = (c-2+len(cups))%len(cups)+1
    while dest_c in group:
        dest_c = (dest_c-2+len(cups))%len(cups)+1

    # Place pGroup to destination
    pDest = cups[dest_c]
    pGroup[1][1][1] = pDest[1]
    pDest[1] = pGroup

    # Advance one cup
    pHead = pHead[1]


# Print output
PrintSequence( cups[1], 10 )


# right sequence -> 1  778214  369089  81176  411202  803145  154538  77674  503696  904208
# right -> 778214 * 369089  =  287230227046
