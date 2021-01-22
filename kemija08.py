#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

cases = list(inp())[:-1]
vocal = ['a', 'i', 'u', 'e', 'o']

n = 0

while n <= len(cases)-1:
    if cases[n] in vocal:
        del(cases[n+1:n+3])
    else:
        pass
    n = n + 1

print("".join(cases))