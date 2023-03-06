#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 03 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateValues():
    if 0:
        str = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line

image = list( IterateValues() )
WIDTH = len(image[0])
HEIGHT = len(image)

def GetMap( row, col ):
    global image
    return image[row][col]

def IterMap( element ):
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if image[row][col] == element:
                yield row, col

STEP_X = 3
STEP_Y = 1

x = 0
y = 0
tree_cnt = 0
while y < HEIGHT:
    if GetMap( y, x ) == '#':
        tree_cnt += 1
    x =  (x+STEP_X) % WIDTH
    y += STEP_Y
print( tree_cnt )
