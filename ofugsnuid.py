#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

cases = int(inp())
lst = []
for x in range(cases):
    lst.append(str(inp())[:-1])

for y in list(reversed(lst)):
    print(y)