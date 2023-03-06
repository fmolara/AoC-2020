#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 20 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy, math



def IterateLines():
    if 0:
        str = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def IterImages():
    def _GetImages(it):
        id, img = 0, None
        try:
            line = next(it)
            if not line:
                print("empty")

            assert line[:5] == "Tile " and  line[-1:] == ':', line
            id = int(line[5:-1])

            line = next(it)
            img = numpy.array( [[c] for c in line] )
            while True:
                line = next(it)
                if not line:
                    break
                img = numpy.append( img, [[c] for c in line], axis=1 )
        except StopIteration:
            pass
        return id, img

    it = IterateLines()
    while True:
        id, img = _GetImages(it)
        if id > 0  and img is not None:
            yield id, img
        else:
            break


def IterTiles():
    global images
    for idx in range(len(images)):
        for rot in range(4):
            for x_flip in (False, True):
                for y_flip in (False, True):
                    yield idx, rot, x_flip, y_flip


def PrintImage( img ):
    for y in range(img.shape[1]):
        line = ''.join( [img[x, y] for x in range(img.shape[0])] )
        print( line )


def GetImage( idx, rot, x_flip, y_flip ):
    global images, tiles

    assert 0 <= idx < len(images)
    assert 0 <= rot < 4

    img = images[idx][1]

    if y_flip:   img = numpy.flip( img, axis = 0 )
    if x_flip:   img = numpy.flip( img, axis = 1 )
    if rot > 0:  img = numpy.rot90( img, k = rot )

    return img


def GetTile( t ):
    global tiles

    idx, rot, x_flip, y_flip = tiles[t]
    return GetImage( idx, rot, x_flip, y_flip )


images = tuple([(id, img)  for id, img in IterImages()])
#print(images)

tiles = [tile for tile in IterTiles()]
print(tiles)


if 0:
    solt = numpy.array( [ [ 18, 114, 98],
                          [  2,  50, 66],
                          [128,  85, 33] ] )
else:
    solt = numpy.array( [ [ 305,  706, 2245, 2162, 1106, 1831, 1648, 1863, 1700, 1127,  693, 2209],
                          [ 928, 2066, 1591,  658, 1684,  848, 1191, 1717,  196,   66, 1088, 1920],
                          [2177, 1568,   55,  401,  964, 1009, 1254, 1968, 2050, 1430, 2032, 1174],
                          [ 562, 1204, 1031,  789, 1296, 1959, 1793, 1495,  546, 1537,  433,  997],
                          [ 164, 1879, 1780, 1381, 2116, 1269,  772,  118, 2018,  631,  213,  640],
                          [1761,  724, 1366,  244, 1218, 2096,  480,  592,   33, 1072,  130, 1041],
                          [ 359, 1232,    2, 1314,  464,  501,  374,  257,  916,  336, 2005, 2260],
                          [ 834, 1057, 2082, 2277, 2288,  951,  146,  226,   84,  517,  420,  903],
                          [  17, 1159, 1346,  455, 1844,  752, 1984,  290, 2228,  391, 2198, 1557],
                          [ 818,  870,  278, 1623, 1462,   96, 1440, 1668, 1734,  325, 1906, 1746],
                          [ 580, 1412,  612, 1604, 1477,  740,  176, 1813, 1285, 2150, 1510, 1890],
                          [1527, 1330, 1138, 1937, 1634,  805,  678,  530, 1392,  976, 2130,  884] ] )

if 1:
    # output solt
    print( "--- solt ---" )
    for y in range(solt.shape[1]):
        print( [solt[x, y] for x in range(solt.shape[0])] )

    # output images[solt].id
    print( "--- ID ---" )
    for y in range(solt.shape[1]):
        print( [images[tiles[solt[x, y]][0]][0] for x in range(solt.shape[0])] )

B = 1
for yt in range(solt.shape[1]):
    imgs = [GetTile( solt[xt, yt] )  for xt in range(solt.shape[0])]
    #imgs = [GetImage( tiles[solt[xt, yt]][0], 0, False, False )  for xt in range(solt.shape[0])]
    for y in range( B, imgs[0].shape[1]-B ):
        for img in imgs:
            print( ''.join( [img[x, y] for x in range( B, img.shape[0]-B )] ), end='' )
        print()

#--- tiles ---
#[19, 58, 136, 35, 10, 110, 22, 52, 1, 51, 36, 95]
#[44, 129, 98, 75, 117, 45, 77, 66, 72, 54, 88, 83]
#[140, 99, 3, 64, 111, 85, 0, 130, 84, 17, 38, 71]
#[135, 41, 25, 49, 86, 15, 82, 142, 28, 101, 100, 121]
#[69, 105, 60, 81, 132, 76, 29, 143, 115, 91, 92, 102]
#[114, 53, 63, 122, 79, 131, 31, 59, 47, 6, 46, 50]
#[103, 74, 78, 112, 48, 30, 23, 9, 124, 90, 11, 42]
#[116, 107, 123, 93, 7, 37, 16, 14, 18, 104, 113, 33]
#[106, 12, 128, 34, 126, 2, 57, 5, 139, 108, 80, 87]
#[70, 4, 89, 96, 39, 67, 21, 32, 24, 20, 134, 61]
#[43, 68, 127, 27, 13, 8, 125, 26, 137, 119, 94, 133]
#[138, 120, 73, 62, 40, 65, 141, 56, 97, 109, 118, 55]
#
#--- ID ---
#[2711, 2137, 1061, 3917, 3343, 1759, 2647, 3449, 1451, 2879, 1801, 1789]
#[3389, 1657, 3119, 3697, 2843, 2663, 3323, 3911, 1409, 3391, 1471, 2803]
#[1109, 1607, 1117, 1201, 3203, 3517, 3011, 3433, 3607, 3049, 1733, 1579]
#[3191, 2957, 1291, 1483, 3613, 3709, 2203, 2729, 1741, 1951, 2089, 1231]
#[3631, 2801, 1237, 3089, 2917, 2777, 1913, 3533, 1381, 3919, 2477, 3373]
#[1999, 1373, 3733, 1721, 2063, 2383, 3461, 2837, 2591, 1301, 3061, 1543]
#[1619, 3671, 3259, 3877, 2333, 1069, 2543, 1559, 2437, 3623, 2207, 3463]
#[3137, 3659, 2797, 1091, 1103, 1213, 1423, 3361, 3907, 2069, 3319, 1901]
#[1753, 2161, 2357, 2267, 3559, 2003, 1493, 2713, 1039, 1097, 2707, 3823]
#[3691, 2671, 3779, 1667, 2473, 1723, 2351, 1787, 3947, 1307, 1217, 1811]
#[3299, 1297, 1181, 2243, 2969, 1129, 3739, 3001, 2903, 1163, 3929, 2887]
#[2417, 2381, 1873, 1979, 2657, 1637, 2819, 1621, 1847, 1583, 3413, 1453]
#
# right -> 17032646100079
