#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 24 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def ParseLine(line):
    i = 0
    while i < len(line):
        if line[i] in ('w', 'e'):
            yield line[i]
            i += 1
        else:
            assert line[i] in ('n', 's')
            assert i+1 < len(line)
            yield line[i:i+2]
            i += 2


moves = {
    'w':  numpy.array( ( -1,  0 ) ),
    'e':  numpy.array( ( +1,  0 ) ),

    'nw': numpy.array( (  0, -1 ) ),
    'se': numpy.array( (  0, +1 ) ),

    'ne': numpy.array( ( +1, -1 ) ),
    'sw': numpy.array( ( -1, +1 ) ),
}


def GetInitialTiles():
    tiles = {}
    for line in IterateLines():
        #print(line)
        pos = (0, 0)
        for cmd in ParseLine(line):
            #print( "  ", cmd, end='' )
            pos = tuple( [pos[i] + moves[cmd][i]  for i in range(len(pos))] )
            #print( " ", pos )
        tiles[pos] = (tiles.get( pos, 0 )+1)%2
    return tiles


def PrintTiles( tiles ):
    y_min = min( y for x, y in tiles )
    y_max = max( y for x, y in tiles )
    x_min = min( x for x, y in tiles )
    x_max = max( x for x, y in tiles )
    for y in range(y_min, y_max+1):
        line = ''.join( ['#' if tiles.get((x,y), 0) else ' '   for x in range(x_min, x_max+1)] )
        print( line )


def CountTiles( tiles ):
    return sum( tiles[x, y] for x, y in tiles )


def CountAdjacent( tiles, pos ):
    cnt = 0
    for m in ('w', 'e', 'nw', 'se', 'ne', 'sw'):
        _pos = tuple( [pos[i] + moves[m][i]  for i in range(len(pos))] )
        cnt += tiles.get( _pos, 0 )
    return cnt


def FlipTiles( tiles0 ):
    tiles1 = {}
    y_min = min( y for x, y in tiles )
    y_max = max( y for x, y in tiles )
    x_min = min( x for x, y in tiles )
    x_max = max( x for x, y in tiles )
    for y in range(y_min-1, y_max+2):
        for x in range(x_min-1, x_max+2):
            pos = (x, y)
            cnt = CountAdjacent( tiles0, pos )
            if tiles0.get(pos, 0) == 1:  # Black?
                if cnt == 0  or  cnt > 2:
                    if pos in tiles1: del tiles1[pos]
                else:
                    tiles1[pos] = 1
            else: # White
                if cnt == 2:
                    tiles1[pos] = 1
                else:
                    if pos in tiles1: del tiles1[pos]
    return tiles1


tiles = GetInitialTiles()
PrintTiles( tiles )
print( "initial: {}".format( CountTiles( tiles ) ) )
for day in range(1, 101):
    tiles = FlipTiles( tiles )
    print( "day {}: {}".format( day, CountTiles( tiles ) ) )
#PrintTiles( tiles )

# right -> 3608
