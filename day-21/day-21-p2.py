#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 21 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def ParseInput():
    def ParseLine(line):
        i = line.find('(')
        assert i >= 0  and line[-1] == ')'
        lhs = line[:i-1].split(' ')
        rhs = line[i+1:-1].split(' ')
        assert rhs[0] == "contains"
        #print( lhs, rhs[1:] )
        return tuple(lhs), tuple([s[:-1] if s[-1]==',' else s for s in rhs[1:]])

    def AddList( lst, entry ):
        if entry in lst:
            return False
        return True

    all_ingredients = {}
    all_allergens = {}
    all_foods = []
    for line in IterateLines():
        ingredients, allergens = ParseLine(line)
        #print( "ingredients = ", ingredients )
        #print( "allergens = ", allergens )

        for ingr in ingredients:
            if ingr not in all_ingredients:
                all_ingredients[ingr] = (len(all_ingredients), set())
            all_ingredients[ingr][1].update(allergens)
        for allr in allergens:
            if allr not in all_allergens:
                all_allergens[allr] = (len(all_allergens), set(ingredients))
            else:
                all_allergens[allr][1].intersection_update(ingredients)
        all_foods.append( ingredients )

    #hypo = numpy.full( (len(all_ingredients), len(all_allergens)), 0, dtype=int )
    #for allr, (iallr, ingredients) in all_allergens.items():
    #    for ingr in ingredients:
    #        iingr = all_ingredients[ingr][0]
    #        hypo[iingr, iallr] += 1

    return all_ingredients, all_allergens, all_foods



def Visit(all_ingredients, all_allergens, allr_path):
    def _Visit(ipath, sol):
        nonlocal all_ingredients, all_allergens, allr_path

        if ipath == len(allr_path):
            yield sol
        else:
            allr = allr_path[ipath]
            for ingr in all_allergens[allr][1]:
                if ingr in sol: # Each allergen is found in exactly one ingredient
                    continue
                for s in _Visit(ipath+1, sol+[ingr]):
                    yield s

    for s in _Visit(0, []):
        yield s




all_ingredients, all_allergens, all_foods = ParseInput()
if 1:
    print("--- all ingredients ---")
    for k, v in all_ingredients.items():
        print(k, v)
    print("--- all allergens ---")
    for k, v in all_allergens.items():
        print(k, v)
    print("--- all foods ---")
    for ifood, food in enumerate(all_foods):
        print(ifood, food)
    #print("--- hypo ---")
    #print(hypo)


print("--- free ingredients ---")
it = iter(Visit(all_ingredients, all_allergens, [allr for allr in all_allergens]))
sol = next(it)
assert next(it, None) is None

print(sol)
dangerous = [(allr, ingr) for allr, ingr in zip(all_allergens, sol)]
print(dangerous)
dangerous = sorted(dangerous, key=lambda e: e[0])
print(dangerous)
#dangerous = sorted(sol)
#, key=lambda e: len(e[1]))]
print(dangerous)
print(','.join( [ingr for allr, ingr in dangerous] ))
# right -> "bcdgf,xhrdsl,vndrb,dhbxtb,lbnmsr,scxxn,bvcrrfbr,xcgtv"
