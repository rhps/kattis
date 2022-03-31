#!/usr/bin/env python

"""
Digit Swap

https://open.kattis.com/problems/digitswap
"""
from copy import copy
import sys
def inp():
    return sys.stdin.readline()

n = list(inp())[:-1]

print(''.join([n[1], n[0]]))