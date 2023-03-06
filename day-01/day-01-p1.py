#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 01 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateValues():
    with open('input.txt') as f:
        for line in f.readlines():
            yield int(line)

def FindSum2020( N ):
    for lst in itertools.combinations(IterateValues(), N):
        if sum(lst) == 2020:
            yield lst

for lst in FindSum2020(2):
    print( lst, numpy.prod(lst) )
