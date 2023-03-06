#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 11 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line




def GetMap( image, row, col ):
    assert 0 <= row < image.shape[0] and 0 <= col < image.shape[1]
    return image[row][col]

def SetMap( image, row, col, item ):
    image[row][col] = item

def PrintMap( image ):
    for row in range(image.shape[0]):
        print( '{:4d}: '.format(row), end='' )
        print( "".join( [image[row][col] for col in range(image.shape[1])] ) )

def IterMap( image, item ):
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            if image[row][col] == item:
                yield row, col

def EqualMaps( image_0, image_1 ):
    return numpy.array_equal( image_0, image_1 )


directions = (
    ( -1,  -1 ), ( -1, 0 ), ( -1, +1 ),
    (  0,  -1 ),            (  0, +1 ),
    ( +1,  -1 ), ( +1, 0 ), ( +1, +1 ),
)

def IterPos( image, pos ):
    for row, col in directions:
        if 0 <= pos[0]+row < image.shape[0] and \
           0 <= pos[1]+col < image.shape[1]:
            yield pos[0]+row, \
                  pos[1]+col

def CountItems( image, pos, item ):
    return sum( 1 for row, col in IterPos( image, pos ) if GetMap( image, row, col ) == item )

def TurnSeats( image_0 ):
    image_1 = image_0.copy()
    for row in range(image_0.shape[0]):
        for col in range(image_0.shape[1]):
            # Rule 1 : If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if GetMap( image_0, row, col ) == 'L' and CountItems( image_0, (row, col), '#' ) == 0:
                SetMap( image_1, row, col, '#' )
            # Rule 2 : If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty
            elif GetMap( image_0, row, col ) == '#' and CountItems( image_0, (row, col), '#' ) >= 4:
                SetMap( image_1, row, col, 'L' )
    return image_1



_image = numpy.array( [[item for item in line] for line in IterateLines()] )

image = [ _image, _image ]
for i in range(1, 10**9):
    i0 = (i-1)%2
    i1 = (i+0)%2
    image[i1] = TurnSeats( image[i0] )
    if EqualMaps( image[i0], image[i1] ):
        break

PrintMap( image[i1] )
print( sum( 1 for row, col in IterMap( image[i1], '#' ) ) )

