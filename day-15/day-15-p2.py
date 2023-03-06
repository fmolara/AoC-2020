#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 15 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy
import math



def GetLine( idx = -1 ):
    line = ( ("0,3,6", 175594 )
           , ("1,3,2", 2578   )
           , ("2,1,3", 3544142)
           , ("1,2,3", 261214 )
           , ("2,3,1", 6895259)
           , ("3,2,1", 18     )
           , ("3,1,2", 362    )
           )
    if idx < 0:
        return "16,1,0,18,12,14,19", None
    else:
        return line[idx]


def ParseInput( line ):
    for n in line.split(','):
        yield int(n)


def GetDiff( n, history, turn ):
    assert n in history

    turn_1, turn_0 = history[n]
    return turn_1-turn_0 if turn_0 is not None else turn-turn_1


def HasSpoken( n, history ):
    if n not in history:
        return False

    turn_1, turn_0 = history[n]
    return turn_0 is not None


def Spoke( n, history, turn ):
    if n in history:
        turn_1, turn_0 = history[n]
        diff = GetDiff( n, history, turn )
        history[n] = (turn, turn_1)
    else:
        diff = None
        history[n] = (turn, None)
    return diff


def Turns( line, MAX_TURN = 30000000 ):
    turn = 1
    last = None
    history = {}
    for n in ParseInput( line ):
        history[n] = (turn, None)

        last = n
        turn += 1

    while turn <= MAX_TURN:
        #print( turn, last, history )
        if HasSpoken( last, history ):
            spoke = GetDiff( last, history, turn )
        else:
            spoke = 0

        if turn%1000000 == 0:
            print( "turn: {}, pogress: {:.1f}, last: {}, spoke: {}".format( turn, turn/MAX_TURN*100.0, last, spoke ) )

        Spoke( spoke, history, turn )
    
        turn += 1
        last = spoke
    return spoke

line, res = GetLine(  )
print( Turns( line ), res )
