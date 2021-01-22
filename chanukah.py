#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

cases = int(inp())

for x in range(cases):
    a, b = map(int, inp().split())
    tot = 0
    for y in range(1,b+1):
        tot = tot + y + 1
    print(a, tot)