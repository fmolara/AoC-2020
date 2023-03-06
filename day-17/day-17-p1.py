#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 17 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """.#.
..#
###"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def MakeCube():
    it = IterateLines()
    res = GetEmptyCube()
    try:
        line = next(it)
        res = numpy.array( [[[c]] for c in line] )
        while True:
            line = next(it)
            res = numpy.append( res, [[[c]] for c in line], axis=1 )
    except StopIteration:
        pass
    return res


def GetEmptyCube( shape = (0, 0, 0) ):
    return numpy.full( shape, '.' )


def ExpandyCube( cube_in, delta ):
    hdelta = delta//2
    cube_out = GetEmptyCube( [s+delta for s in cube_in.shape] )
    for ii in itertools.product( *[range(cube_in.shape[i]) for i in range(cube_in.ndim)] ):
        jj = tuple(map(operator.add, ii, (hdelta,)*cube_in.ndim))
        cube_out[jj] = cube_in[ii]
    return cube_out
    


def IsValidCoo( cube, row, col ):
    return 0 <= row < cube.shape[0] and 0 <= col < cube.shape[1]

def PrintCube( cube ):
    for z in range(cube.shape[2]):
        print( " "*z, "z = ", z )
        for y in range(cube.shape[1]):
            line = ''.join( [cube[x, y, z] for x in range(cube.shape[0])] )
            print( " "*z, line )

def IterCube( cube, item ):
    for row in range(cube.shape[0]):
        for col in range(cube.shape[1]):
            if cube[row, col] == item:
                yield row, col

def EqualCubes( cube_0, cube_1 ):
    return numpy.array_equal( cube_0, cube_1 )


def IterDirections( ndim ):
    for ii in itertools.product( *[range(-1,2) for i in range(ndim)] ):
        if all(ii[i] == 0 for i in range(ndim)):
            continue
        yield ii


def IterNeighbors( cube, pos ):
    assert len(pos) == cube.ndim

    for delta in IterDirections( cube.ndim ):
        assert len(delta) == len(pos)
        delta_pos = tuple(map(operator.add, pos, delta))
        if all(0 <= delta_pos[i] < cube.shape[i] for i in range(len(delta_pos))):
            yield delta_pos


def CountNeighbors( cube, pos, kind ):
    return sum( 1 if cube[ii] == kind else 0  for ii in IterNeighbors( cube, pos ) )


def Count( cube, kind ):
    return sum(1 if cube[ii] == kind else 0 for ii in itertools.product( *[range(cube.shape[i]) for i in range(cube.ndim)] ))


def DoCycle( cube_in ):
    cube_out = GetEmptyCube( cube_in.shape )
    for ii in itertools.product( *[range(cube_in.shape[i]) for i in range(cube_in.ndim)] ):
        if cube_in[ii] == '#':
            cube_out[ii] = '#' if 2 <= CountNeighbors( cube_in, ii, '#' ) <= 3 else '.'
        else:
            assert cube_in[ii] == '.'
            cube_out[ii] = '#' if 3 == CountNeighbors( cube_in, ii, '#' ) else '.'
    return cube_out


NUM_CYCLES = 6

cube = MakeCube()
#print( "-"*10 )
#PrintCube( cube )
cube = ExpandyCube( cube, 2*NUM_CYCLES )
#print( "-"*10 )
#PrintCube( cube )
for cycle in range(NUM_CYCLES):
    print("cycle = ", cycle )
    cube = DoCycle( cube )
    #print( "-"*10 )
    #PrintCube( cube )
print(Count( cube, '#' ))

# right -> 372
