#!/usr/bin/env python

"""
Parking

https://open.kattis.com/problems/parking2
"""
import sys
def inp():
    return sys.stdin.readline()


for x in range(int(inp())):
    case = int(inp())
    park = sorted(list(map(int, inp().split())))
    
    tot = 0
    for y in range(case-1):
        tot = tot + (park[y+1] - park[y])
    
    print(tot*2)