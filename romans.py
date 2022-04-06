#!/usr/bin/env python

"""
Stopwatch

https://open.kattis.com/problems/stopwatch
"""
from copy import copy
from math import ceil
from random import sample
import sys
def inp():
    return sys.stdin.readline()

X = float(inp())

print(int(round(X*5280000/4854, 0)))