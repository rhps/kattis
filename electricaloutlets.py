#!/usr/bin/env python

"""
Electrical Outlets

https://open.kattis.com/problems/electricaloutlets
"""
import sys
def inp():
    return sys.stdin.readline()

cases = int(inp())

for x in range(cases):
    case = list(map(int, inp().split()))[1:]
    tot = 0
    for x in case:
        tot = tot + x - 1
    print(tot+1)