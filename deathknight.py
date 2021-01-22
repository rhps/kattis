#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

cases = int(inp())
lose = 0
for x in range(cases):
    case = list(inp())[:-1]
    for y in range(len(case)-1):
        if case[y] == "C" and case[y+1] == "D":
            lose = lose + 1
print(cases-lose)