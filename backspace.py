#!/usr/bin/env python

"""
Backspace

https://open.kattis.com/problems/backspace
"""
import sys

inp = list(sys.stdin.readline()[:-1])

outp = []
for x in inp:
    if x == "<":
        outp.pop()
    else:
        outp.append(x)
print("".join(outp))