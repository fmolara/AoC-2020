#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 16 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
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
if 1:
    for rule in rules:
        print( rule )

label = next(it)
assert label == "your ticket:"
my_ticket = GetTicket( it )
print( "my_ticket = ", my_ticket )
assert next(it) == ""

nby_tickets = []
label = next(it)
assert label == "nearby tickets:"
while True:
    nby_ticket = GetTicket( it )
    if not nby_ticket:
        break
    if all( TestRules_Any( rules, val ) for val in nby_ticket ):
        nby_tickets.append( nby_ticket )
nby_tickets = tuple(nby_tickets)
if 0:
    for i, nby_ticket in enumerate(nby_tickets):
        #print( "{}: {}".format(i, nby_ticket) )
        print( nby_ticket )



def ItemValidPerms( rules, tickets ):
    def _EnumChoices():
        for rule_idx, rule in enumerate(rules):
            cols = []
            for col in range(len(rules)):
                if all( TestRule( rule, ticket[col] ) for ticket in nby_tickets ):
                    cols.append(col)
            yield rule_idx, cols
            

    def _ItemValidPerms( perm, choices ):
        #print( "  "*(len(rules)-len(choices)), "->", perm )
        if not choices:
            assert all( idx >= 0 for idx in perm ), perm
            yield perm
        else:
            rule_idx, cols = choices[0]
            assert rule_idx not in perm

            for col in cols:
                if perm[col] >= 0:
                    continue
                _perm = perm.copy()
                _perm[col] = rule_idx

                for res in _ItemValidPerms( _perm, choices[1:] ):
                    yield res

    for ticket in tickets:
        assert len(ticket) == len(rules)

    choices = tuple([(rule_idx, tuple(cols)) for rule_idx, cols in sorted(_EnumChoices(), key=lambda e: len(e[1]))])
    if 0:
        for rule_idx, cols in choices:
            print( rule_idx, cols )
    for perm in _ItemValidPerms( [-1]*len(rules), choices ):
        yield perm

if 1:
    for perm in ItemValidPerms( rules, nby_tickets ):
        break
else:
    perm =  [11, 1, 5, 13, 10, 12, 14, 16, 18, 19, 17, 6, 2, 9, 15, 3, 4, 0, 7, 8]
print( "perm = ", perm )


def TestTicket( rule, ticket ):
    pass

for ticket in (my_ticket,)+nby_tickets:
    for idx in range(len(rules)):
        if not TestRule( rules[perm[idx]], ticket[idx] ):
            print("---")

acc = 1
for idx in range(len(rules)):
    print( idx, perm[idx], rules[perm[idx]], my_ticket[idx] )
    if rules[perm[idx]][0].find("departure") == 0:
        acc *= my_ticket[idx]
print(acc)
# wrong -> 650
# wrong -> 752
# right -> 2766491048287

