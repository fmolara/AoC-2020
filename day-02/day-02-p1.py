#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 02 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    with open('input.txt') as f:
        for line in f.readlines():
            yield line

def LineToValues(line):
    lhs = line.split(':')[0].strip()
    rhs = line.split(':')[1].strip()

    lhs_range = lhs.split(' ')[0]
    lhs_char =  lhs.split(' ')[1]

    return [int(x) for x in lhs_range.split('-')], lhs_char, rhs


def IsValidLine(line):
    (m, M), c, pwd = LineToValues(line)
    cnt = pwd.count(c)
    return m <= cnt <= M


#for line in IterateLines():
#    if IsValidLine(line):
#        print( LineToValues(line) )

valid_cnt = sum(1 for line in IterateLines() if IsValidLine(line))
print( valid_cnt )
