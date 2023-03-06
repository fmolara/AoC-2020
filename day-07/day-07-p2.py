#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 07 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    elif 0:
        str = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def LineToRule(line):
    assert line[-1:] == '.'
    line = line[:-1]

    line = line.replace(' bags', '') \
               .replace(' bag', '')

    lhs = line.split(' contain ')[0]
    rhs = line.split(' contain ')[1]

    node = {}
    for part in rhs.split(', '):
        i = part.find(' ')
        if part[:i] == 'no':
            continue
        qty = int(part[:i])
        bag = part[i+1:]
        node[bag] = qty

    return lhs, node


def IterateRules():
    for line in IterateLines():
        yield LineToRule(line)


def MakeRules():
    rules = {}
    for key, node in IterateRules():
        rules[key] = node
    return rules


def IterContained(rules, bag):
    for _bag, cnt in rules[bag].items():
        yield _bag, cnt


def CountContained(rules, bag):
    res = 0
    for _bag, cnt in IterContained(rules, bag):
        res += cnt*(1+CountContained(rules, _bag))
    return res


rules = MakeRules()
print(CountContained(rules, 'shiny gold'))

#print( sum( [GroupCount(grp) for grp in IterateGroups()] ) )
