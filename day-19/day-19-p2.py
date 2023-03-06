#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 19 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
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


if 1:
    rules[8] = ((42,),(42,8))
    rules[11] = ((42,31),(42,11,31))

cnt = 0
for msg in messages:
    if any( res and _len == len(msg)  for res, _len in MatchValids( msg, rules ) ):
        print( msg)
        cnt += 1
print( cnt )

# right -> 400
