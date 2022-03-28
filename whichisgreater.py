#!/usr/bin/env python

"""
Which is Greater?

https://open.kattis.com/problems/whichisgreater
"""
import sys
def inp():
    return sys.stdin.readline()

a, b = inp().split()

if int(a) > int(b):
    print(1)
else:
    print(0)