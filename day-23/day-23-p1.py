#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 23 / Part 1
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


def GetCups():
    return [int(c)  for c in GetLine()]

cups = GetCups()
LEN = len(cups)

for turn in range(101):
    print(turn, cups)

    c, three = cups[0], cups[1:4]
    del cups[0:4]

    # Find insertion point
    for i in range(1, LEN):
        c_dest = (c-1-i+LEN)%LEN+1
        if c_dest in cups:
            break
    else:
        assert False
    i = cups.index(c_dest)
    cups[i+1:i+1] = three
    cups.append(c)

# right -> 65432978
