#!/usr/bin/env python

"""
Pyramids

https://open.kattis.com/problems/pyramids
"""
from copy import copy
import sys
def inp():
    return sys.stdin.readline()

n = int(inp())

i = 1
nsum = 0
j = 0
while True:
    if nsum > n:
        break
    else:
        nsum = nsum + i*i
        i = i + 2
        j = j + 1

print(j-1)