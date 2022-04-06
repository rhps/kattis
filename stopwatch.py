#!/usr/bin/env python

"""
Stopwatch

https://open.kattis.com/problems/stopwatch
"""
from copy import copy
from random import sample
import sys
def inp():
    return sys.stdin.readline()

n = int(inp())
tmp = 0
run = False

for x in range(n):
    if (x%2 == 0):
        tmp = int(inp()) - tmp
        run = True
    else:
        tmp = int(inp()) - tmp
        run = False

if run:
    print('still running')
else:
    print(tmp)