#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 16 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def IterRules( it ):
    line = next(it)
    while line:
        key = line.split(': ')[0]
        rhs = line.split(': ')[1]
        yield key, tuple([tuple([int(n) for n in term.split('-')]) for term in rhs.split(' or ')])

        line = next(it)


def GetTicket( it ):
    try:
        line = next(it)
        return tuple([int(n) for n in line.split(',')])
    except StopIteration:
        return ()


def TestRule( rule, val ):
    name, terms = rule
    return any( m <= val <= M for (m, M) in terms )


def TestRules_Any( rules, val ):
    return any( TestRule( rule, val ) for rule in rules )



it = IterateLines()
rules = tuple([rule for rule in IterRules( it )])
print( "rules = ", rules )

label = next(it)
assert label == "your ticket:"
my_ticket = GetTicket( it )
print( "my_ticket = ", my_ticket )
assert next(it) == ""

acc = 0
label = next(it)
assert label == "nearby tickets:"
while True:
    nby_ticket = GetTicket( it )
    if not nby_ticket:
        break
    print( "nby_ticket = ", nby_ticket )
    for val in nby_ticket:
        if not TestRules_Any( rules, val ):
            print( "  ", val )
            acc += val
print( acc )            
# right -> 27898
