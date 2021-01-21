#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

for x in range(int(inp())):
    cases = list(map(int, inp().split()))
    
    for y in range(1,cases[0]):
        if (cases[y+1] - cases[y]) == 1:
            pass
        else:
            print(y+1)
            break