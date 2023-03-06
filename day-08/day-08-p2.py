#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Advent Of Code 2020
# Day 08 / Part 2
#
# (c) 2020-2023 Federico Molara <federico@molara.net>
# This code is licensed under MIT license (see LICENSE.txt for details)

import itertools
import numpy



def IterateLines():
    if 0:
        str = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        for line in str.splitlines():
            yield line
    else:
        with open('input.txt') as f:
            for line in f.read().splitlines():
                yield line


def LineToAssembly(line):
    lhs = line.split(' ')[0]
    rhs = line.split(' ')[1]

    return lhs, int(rhs)


def IterateAssembly():
    for line in IterateLines():
        yield LineToAssembly(line)




class Machine:
    def __init__(self, prog):
        self.prog =  prog.copy()
        self.iflag = [False]*len(prog)
        self.debug = False
        # Registers
        self.acc = 0
        self.pc = 0

    def Nop(self, op):
        self.pc += 1
    def Acc(self, op):
        self.acc += op
        self.pc += 1
    def Jmp(self, op):
        self.pc += op
    micro_code = \
    {
        'nop': Nop,
        'acc': Acc,
        'jmp': Jmp,
    }
    def Run(self):
        while True:
            if self.pc >= len(self.prog):
                return True
            if self.iflag[self.pc]:
                return False
            self.iflag[self.pc] = True

            instr, op = self.prog[self.pc]
            if self.debug:
                print( self.pc, instr, op )
            self.micro_code[instr]( self, op )
        


if 0:
    for instr in IterateAssembly():
        print(instr)
prog = [instr for instr in IterateAssembly()]
for i, (instr, op) in enumerate(prog):
    if instr not in ('nop', 'jmp'):
        continue
    _prog = prog.copy()
    _prog[i] = ('jmp', op) if instr == 'nop' else ('nop', op)
    m = Machine(_prog)
    if m.Run():
        print('Found at', i)
        print(m.acc)
        break
else:
    print('Not found')
