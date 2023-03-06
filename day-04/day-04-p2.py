#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 04 / Part 2
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
    if len(pp) != 8:
        if len(pp) != 7 or 'cid' in pp:
            return False
    for key, val in pp.items():
        if key == 'byr':
            # (Birth Year) - four digits; at least 1920 and at most 2002.
            if not 1920 <= int(val) <= 2002:
                return False
        elif key == 'iyr':
            # (Issue Year) - four digits; at least 2010 and at most 2020.
            if not 2010 <= int(val) <= 2020:
                return False
        elif key == 'eyr':
            # (Expiration Year) - four digits; at least 2020 and at most 2030.
            if not 2020 <= int(val) <= 2030:
                return False
        elif key == 'hgt':
            # (Height) - a number followed by either cm or in:
            #    - If cm, the number must be at least 150 and at most 193.
            #    - If in, the number must be at least 59 and at most 76.
            if len(val) <= 2:
                return False
            ival = int(val[:-2])
            if val[-2:] == 'in':
                if not 59 <= ival <= 76:
                    return False
            elif val[-2:] == 'cm':
                if not 150 <= ival <= 193:
                    return False
            else:
                return False
        elif key == 'hcl':
            # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            if len(val) != 7 or val[0] != '#':
                return False
            for c in val[1:]:
                if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
                    return False
        elif key == 'ecl':
            # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            if val not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
        elif key == 'pid':
            # (Passport ID) - a nine-digit number, including leading zeroes.
            if len(val) != 9:
                return False
            for c in val:
                if not '0' <= c <= '9':
                    return False
        elif key == 'cid':
            # (Country ID) - ignored, missing or not.
            pass
        else:
            return False
    return True



for pp in IterPassports():
    if IsValidPassport(pp):
        print( pp )

valid_cnt = sum(1 for pp in IterPassports() if IsValidPassport(pp))
print( valid_cnt )
