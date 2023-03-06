#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 22 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy, math
import copy



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

    assert player1[0] == 1  and  player2[0] == 2
    return player1[1], player2[1]


def GetSubGame(players):
    sub_players = [cards[1:cards[0]+1].copy()  for cards in players]
    return sub_players


def GuessWinner( players ):
    max_0 = max( players[0] )
    max_1 = max( players[1] )
    if max_0 > max_1:
        return 0
    return None


def PlayTurn( players, path ):
    for ilooser, cards in enumerate(players):
        if not cards:
            return True, (ilooser+1)%len(players)

    if players[0][0] <= len(players[0])-1 and \
       players[1][0] <= len(players[1])-1:
        # Plays sub-game
        sub_players = GetSubGame(players)
        iwinner = GuessWinner( sub_players )
        if iwinner is None:
            iwinner = PlayMatch( sub_players, path )
    else:
        # Normal play
        iwinner = 0 if players[0][0] > players[1][0] else 1
    players[iwinner].append( players[iwinner].pop(0) )
    players[iwinner].append( players[(iwinner+1)%len(players)].pop(0) )
    return False, iwinner


def PlayMatch( players, path = [] ):
    local_history = []
    iwinner, turn = None, 0
    while True:
        #print( "--", '.'.join([str(t) for t in path + [turn]]), "--")
        #for player in players:
        #    print(tuple(player))

        if players in local_history:
            print( "recursion break")
            iwinner = 0
            break
        local_history.append( copy.deepcopy(players) )

        final, iround = PlayTurn( players, path + [turn] )
        if final:
            iwinner = iround
            break
        #print( "Winner = ", players[iround][0] )
        turn += 1
    return iwinner


players = GetDecks()
iwinner = PlayMatch( players )

cards = players[iwinner]
for player in players:
    print(player)
print('-'*10)
for i, card in enumerate(cards):
    print( card, len(cards)-i )
print( sum( card * (len(cards)-i)  for i, card in enumerate(cards) ) )


# too low -> 16818
# too low -> 17923
# wrong   -> 31985
# too low -> 32655  -- no guess

# right   -> 32665

# wrong   -> 33056
# wrong   -> 34174
# wrong   -> 34349
