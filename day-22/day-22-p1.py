#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 22 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy, math



def IterateLines():
    if 0:
        str = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def GetDecks():
    def _GetDeck(it):
        id, cards = 0, None
        try:
            line = next(it)
            if not line:
                print("empty")

            assert line[:7] == "Player " and  line[-1:] == ':', line
            id = int(line[7:-1])

            cards = []
            while True:
                line = next(it)
                if not line:
                    break
                cards.append( int(line) )
        except StopIteration:
            pass
        return id, cards

    it = IterateLines()
    player1 = _GetDeck(it)
    player2 = _GetDeck(it)
    assert next(it, None) is None
    return player1, player2


def PlayTurn( players ):

    if any(not cards  for id, cards in players):
        return None

    top_cards = [(i, cards.pop(0))  for i, (id, cards) in enumerate(players)]
    top_cards = sorted( top_cards, key=lambda e: e[1], reverse=True )

    iwinner = top_cards[0][0]
    players[iwinner][1].extend( [card for i, card in top_cards] )
    return iwinner


players = GetDecks()
for i in range(1, len(players)):
    assert len(players[i][1]) == len(players[i-1][1])
TOTAL_CARDS = sum(len(players[i][1])   for i in range(len(players)))

iwinner, turn = None, 0
while True:
    print( "-- turn ", turn, " --")
    for player in players:
        print(player)
    iround = PlayTurn( players )
    assert TOTAL_CARDS == sum(len(players[i][1])   for i in range(len(players)))
    if iround is None:
        break
    print( "Winner = ", players[iround][0] )

    iwinner = iround
    turn += 1

id, cards = players[iwinner]
for i, card in enumerate(cards):
    print( card, len(cards)-i )
print( sum( card * (len(cards)-i)  for i, card in enumerate(cards) ) )


# right -> 32495