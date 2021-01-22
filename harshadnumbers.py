#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

cases = int(inp())

while True:
    listcases = map(int, list(str(cases)))
    if cases % sum(listcases) == 0:
        print(cases)
        break
    else:
        cases = cases + 1