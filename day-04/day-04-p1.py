#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 04 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def IterPassports():
    pp = {}
    for line in IterateLines():
        if line:
            for kv_str in line.split(' '):
                key = kv_str.split(':')[0]
                val = kv_str.split(':')[1]
                pp[key] = val
        else:
            yield pp
            pp.clear()
    if pp:
        yield pp


def IsValidPassport(pp):
    return len(pp) == 8  or  len(pp) == 7 and 'cid' not in pp


#for pp in IterPassports():
#    print( pp, IsValidPassport(pp) )

valid_cnt = sum(1 for pp in IterPassports() if IsValidPassport(pp))
print( valid_cnt )
