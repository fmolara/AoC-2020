#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 20 / Part 1
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


def PrintImage( img ):
    for y in range(img.shape[1]):
        line = ''.join( [img[x, y] for x in range(img.shape[0])] )
        print( line )


def DigestImage( img ):
    # Returns clock-wise borders
    XM = img.shape[0]-1
    YM = img.shape[1]-1
    top =    ''.join( [img[   x,    0] for x in range(img.shape[0])] )
    right =  ''.join( [img[  XM,    y] for y in range(img.shape[1])] )
    bottom = ''.join( [img[XM-x,   YM] for x in range(img.shape[0])] )
    left =   ''.join( [img[   0, YM-y] for y in range(img.shape[1])] )

    if 1:
        top =    top   .replace('.', '0').replace('#', '1')
        right =  right .replace('.', '0').replace('#', '1')
        bottom = bottom.replace('.', '0').replace('#', '1')
        left =   left  .replace('.', '0').replace('#', '1')
        return (int(top,       2), int(right,       2), int(bottom,       2), int(left,       2)) \
             , (int(top[::-1], 2), int(right[::-1], 2), int(bottom[::-1], 2), int(left[::-1], 2))
    else:
        return (top,       right,       bottom,       left       ) \
             , (top[::-1], right[::-1], bottom[::-1], left[::-1] )



def IterCooOrder( order ):
    for y in range(order+1):
        yield order, y
    for x in range(order):
        yield order-x-1, order


def IterCoo( max_order ):
    for order in range(max_order):
        for x, y in IterCooOrder(order):
            yield x, y


def Visit( images ):
    # placement = (idx, rot, x_flip, y_flip)
    #                     idx =    0..len(images)-1 = image index
    #                     rot =    0..3             = number of clock-wise rotations
    #                     x_flip = False, True      = True if flipped on x axis
    #                     y_flip = False, True      = True if flipped on y axis
    #
    # border = 0:top; 1:right; 2:bottom; 3:left

    def _GetBorder( idx, rot, x_flip, y_flip ):
        nonlocal images
        assert 0 <= idx < len(images)
        assert 0 <= rot < 4

        brd =     images[idx][1][0]
        brd_rev = images[idx][1][1]

        # apply flips
        border_perm = ( 2 if x_flip else 0,
                        3 if y_flip else 1,
                        0 if x_flip else 2,
                        1 if y_flip else 3 )
        reverse =     (x_flip != y_flip)  # every flip inverts the spin, two inversions means non inversion

        # apply rot
        brd =      tuple( [brd    [border_perm[(border-rot+4)%4]]  for border in range(len(brd    ))] )
        brd_rev =  tuple( [brd_rev[border_perm[(border-rot+4)%4]]  for border in range(len(brd_rev))] )

        return brd_rev if reverse else brd     \
             , brd     if reverse else brd_rev \

    def _IterTiles():
        nonlocal images
        for idx in range(len(images)):
            for rot in range(4):
                for x_flip in (False, True):
                    for y_flip in (False, True):
                        brd, brd_rev = _GetBorder( idx, rot, x_flip, y_flip )
                        yield idx, rot, x_flip, y_flip, (brd, brd_rev)

    def _CreateIncidenceMatrix(border, tiles):
        for t0, (idx0, _, _, _, (brd0, brd_rev0)) in enumerate(tiles):
            cnt = 0
            for t1, (idx1, _, _, _, (brd1, brd_rev1)) in enumerate(tiles):
                if idx0 == idx1:
                    continue
                if brd0[border] != brd_rev1[(border+2)%4]:
                    continue
                cnt += 1
            yield cnt

    def _CreateBorderMap(tiles):
        def _AddMap( key, t):
            nonlocal res
            if key not in res:
                res[key] = []
            assert t not in res[key]
            res[key].append( t )

        res = {}
        for t, (idx, rot, x_flip, y_flip, (brd, brd_rev)) in enumerate(tiles):
            _AddMap( (brd[0], None,   None, None  ), t ) # top
            _AddMap( (None,   None,   None, brd[3]), t ) # left
            _AddMap( (brd[0], None,   None, brd[3]), t ) # top-left
            _AddMap( (brd[0], brd[1], None, None  ), t ) # top-right
        return res

    def _IterCompatible( x, y ):
        nonlocal grid, tiles, used, the_map

        if (x, y) == (0, 0):
            #for t in range(len(tiles)):
            for t in (305,311,314,316,881,887,890,892,1523,1525,1528,1534,2211,2213,2216,2222):
                yield t
            return

        match_sides = [None]*4

        # test top side
        if y > 0  and  grid[x, y-1] >= 0:
            _, _, _, _, (brd, brd_rev) = tiles[grid[x, y-1]]
            match_sides[0] = brd_rev[2]  # bottom of other tile must match top of this tile

        # test left side
        if x > 0  and  grid[x-1, y] >= 0:
            _, _, _, _, (brd, brd_rev) = tiles[grid[x-1, y]]
            match_sides[3] = brd_rev[1]  # right of other tile must match left of this tile

        # test right side
        if x+1 < grid.shape[0]  and  grid[x+1, y] >= 0:
            _, _, _, _, (brd, brd_rev) = tiles[grid[x+1, y]]
            match_sides[1] = brd_rev[3]  # left of other tile must match right of this tile

        # ensure bottom side is free
        assert y+1 >= grid.shape[1]  or  grid[x, y+1] < 0

        key = tuple(match_sides)
        if key in the_map:
            for t in the_map[key]:
                if used[tiles[t][0]]:
                    continue
                #idx, rot, x_flip, y_flip, (brd, brd_rev) = tiles[t]
                #assert all( match_sides[i] is None  or  match_sides[i] == brd[i] for i in range(4) )
                yield t

    def _Visit( level=0 ):
        nonlocal grid, path, used

        if level == len(path):
            return True

        x, y = path[level]
        assert grid[x, y] == -1
        for t in _IterCompatible(x, y):
            if level<=9: print( "   "*level, t)
            assert not used[tiles[t][0]]
            used[tiles[t][0]] = True
            grid[x, y] = t
            if _Visit( level+1 ):
                return True
            grid[x, y] = -1
            used[tiles[t][0]] = False
        return False

    order = int(math.sqrt(len(images)))
    assert order**2 == len(images)

    tiles = tuple( [tile for tile in _IterTiles()] )
    for tile in tiles:
        print( tile )
    the_map = _CreateBorderMap(tiles)

    #with open('filename.txt', 'w') as f:
    #    for vals in zip( _CreateIncidenceMatrix(0, tiles), _CreateIncidenceMatrix(1, tiles), _CreateIncidenceMatrix(2, tiles), _CreateIncidenceMatrix(3, tiles) ):
    #        print( vals, file=f )

    grid = numpy.full( (order, order), -1, dtype=int )
    path = [(x,y) for x, y in IterCoo(order)]
    used = [False]*len(images)
    if not _Visit():
        return None
    return grid, numpy.array( [[tiles[grid[x, y]][0] for y in range(grid.shape[1])] for x in range(grid.shape[0])] )


images = tuple([(id, DigestImage(img))  for id, img in IterImages()])
print(images)
solt, sol = Visit( images )
if sol is None:
    print("--- no solutions found ---")
else:
    # output solt
    print( "--- solt ---" )
    for y in range(sol.shape[1]):
        print( [solt[x, y] for x in range(sol.shape[0])] )

    # output sol
    print( "--- sol ---" )
    for y in range(sol.shape[1]):
        print( [sol[x, y] for x in range(sol.shape[0])] )

    # output images[sol].id
    print( "--- ID ---" )
    for y in range(sol.shape[1]):
        print( [images[sol[x, y]][0] for x in range(sol.shape[0])] )

    XM = sol.shape[0]-1
    YM = sol.shape[1]-1
    print(  images[sol[ 0, 0]][0] * images[sol[ 0, YM]][0] \
          * images[sol[XM, 0]][0] * images[sol[XM, YM]][0] )


#--- tiles ---
#[ 305,  928, 2177,  562,  164, 1761,  359,  834,   17,  818,  580, 1527]
#[ 706, 2066, 1568, 1204, 1879,  724, 1232, 1057, 1159,  870, 1412, 1330]
#[2245, 1591,   55, 1031, 1780, 1366,    2, 2082, 1346,  278,  612, 1138]
#[2162,  658,  401,  789, 1381,  244, 1314, 2277,  455, 1623, 1604, 1937]
#[1106, 1684,  964, 1296, 2116, 1218,  464, 2288, 1844, 1462, 1477, 1634]
#[1831,  848, 1009, 1959, 1269, 2096,  501,  951,  752,   96,  740,  805]
#[1648, 1191, 1254, 1793,  772,  480,  374,  146, 1984, 1440,  176,  678]
#[1863, 1717, 1968, 1495,  118,  592,  257,  226,  290, 1668, 1813,  530]
#[1700,  196, 2050,  546, 2018,   33,  916,   84, 2228, 1734, 1285, 1392]
#[1127,   66, 1430, 1537,  631, 1072,  336,  517,  391,  325, 2150,  976]
#[ 693, 1088, 2032,  433,  213,  130, 2005,  420, 2198, 1906, 1510, 2130]
#[2209, 1920, 1174,  997,  640, 1041, 2260,  903, 1557, 1746, 1890,  884]
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
