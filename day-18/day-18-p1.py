#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 18 / Part 1
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import operator
import numpy



def IterateLines():
    if 0:
        str = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def TokenizeExp(line):
    tk = ""
    for c in line:
        if c == ' ':
            if tk: yield int(tk); tk = ''
        elif c in '+*':
            if tk: yield int(tk); tk = ''
            yield c
        elif c in '()':
            if tk: yield int(tk); tk = ''
            yield c
        elif c in '0123456789':
            tk += c
        else:
            assert False, "line = '{}', c = '{}'".format(line, c)
    if tk: yield int(tk); tk = ''


def EvaluateExpr(expr):
    # Grammar:
    #
    #   expr-primary
    #       const
    #       (expr)
    #
    #   expr-sum-prod
    #       expr-primary
    #       expr-sum-prod + expr-primary
    #       expr-sum-prod * expr-primary
    #
    #   expr
    #       expr-sum-prod
    #
    DBG = False

    it, next_tok = iter(expr), None
    def PeekToken():
        nonlocal it, next_tok
        if next_tok is None:
            next_tok = GetToken()
        return next_tok
    def GetToken():
        nonlocal it, next_tok
        res = None
        if next_tok is not None:
            res, next_tok = next_tok, None
        else:
            try:
                res = next(it)
            except StopIteration:
                pass
        return res


    def _ExprPrimary(level):
        assert level >= 0
        if DBG: print( "   "*level, "_ExprPrimary(level={})".format(level) )

        tok = GetToken()
        if DBG: print( "   "*level, "tok = ", tok )

        if tok == '(':
            res = _Expr(level+1)
            assert PeekToken() == ')', "Unexpected tok = {}".format(PeekToken())
            GetToken()
            return res

        if isinstance(tok, int):
            if DBG: print( "   "*level, "<--", tok )
            return tok

        assert False, "Unexpected tok = {}".format(tok)
        if DBG: print( "   "*level, "<--", None )
        return None

    def _ExprSumProd(level):
        assert level >= 0
        if DBG: print( "   "*level, "_ExprSumProd(level={})".format(level) )

        acc = _ExprPrimary(level)
        while PeekToken() in ('+', '*'):
            operator = GetToken()
            if DBG: print( "   "*level, "operator = ", operator )
            operand = _ExprPrimary(level)
            if operator == '+':
                acc += operand
            else:
                acc *= operand
        if DBG: print( "   "*level, "<--", acc )
        return acc

    def _Expr(level):
        assert level >= 0
        if DBG: print( "   "*level, "_Expr(level={})".format(level) )

        return _ExprSumProd(level)

    res = _Expr(0)
    assert PeekToken() is None, "Unexpected tok = {}".format(PeekToken())
    return res


acc = 0
for line in IterateLines():
    #print( "line = ", line, "toekinze = ", [tk for tk in TokenizeExp(line)] )
    val = EvaluateExpr( [tk for tk in TokenizeExp(line)] )
    print( "line = ", line, "eval = ", val )
    acc += val
print( "acc = ", acc )

# right -> 4297397455886
