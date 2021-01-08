#!/usr/bin/env python

"""
ABC

https://open.kattis.com/problems/abc
"""
import sys

abc = sorted(list(map(int, sys.stdin.readline().split())))
order = list(sys.stdin.readline())
outp = []

for x in order:
    if x == "A":
        outp.append(abc[0])
    elif x == "B":
        outp.append(abc[1])
    elif x == "C":
        outp.append(abc[2])
    else:
        pass

print(" ".join(map(str, outp)))