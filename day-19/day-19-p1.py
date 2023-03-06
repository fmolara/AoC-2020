#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 19 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def ParseInput():
    def ParseRule(line):
        def IterClause(clause):
            for term in clause.split(' '):
                yield term[1:-1] if term[0] == '"' else int(term)
        def MakeClause(clause):
            lst = [term for term in IterClause(clause)]
            if len(lst) == 1  and  isinstance(lst[0], str):
                return lst[0]
            return tuple(lst)
        lhs = line.split(': ')[0].strip()
        rhs = line.split(': ')[1].strip().split(' | ')
        return int(lhs), tuple([MakeClause(clause) for clause in rhs])

    def ParseMessage(line):
        return line

    rules = {}
    messages = []
    it = iter(IterateLines())
    try:
        line = next(it)
        while line:
            rule_key, rule_val = ParseRule(line)
            rules[rule_key] = rule_val
            line = next(it)

        messages = [ParseMessage(line) for line in it]
                
    except StopIteration:
        pass
    return rules, messages



def MatchValids( msg, rules, key = 0, level = 0 ):
    def _IterClause( msg, clause ):
        nonlocal rules, level
        if not clause:
            yield True, 0
            return

        for res, _len in MatchValids( msg, rules, clause[0], level+1 ):
            if not res:
                continue

            for _res, __len in _IterClause( msg[_len:], clause[1:] ):
                yield _res, _len+__len

    DBG = 0
    if DBG: print( "  "*level, "msg = {}, key = {} -> {}".format(msg, key, rules[key]) )

    if not msg:
        if DBG: print( "  "*level, "<<-- {}".format(False, 0) )
        yield False, 0

    for clause in rules[key]:
        if DBG: print( "  "*level, "clause = {}".format(clause) )
        if isinstance(clause, str):
            if msg.find(clause) == 0:
                if DBG: print( "  "*level, "<<-- {}".format((True, len(clause))) )
                yield True, len(clause)
            else:
                if DBG: print( "  "*level, "<<-- {}".format((False, None)) )
                yield False, 0
        else:
            for res, _len in _IterClause( msg, clause ):
                if res:
                    if DBG: print( "  "*level, "<<-- {}".format((True, _len)) )
                    yield res, _len


rules, messages = ParseInput()

if 1:
    for rule_key, rule_val in rules.items():
        print("{}: {}".format(rule_key, rule_val))


cnt = 0
for msg in messages:
    if any( res and _len == len(msg)  for res, _len in MatchValids( msg, rules ) ):
        print( msg)
        cnt += 1
print( cnt )

# right -> 216
