#!/usr/bin/env python

"""
Triangle Area

https://open.kattis.com/problems/triarea
"""
import sys
def inp():
    return sys.stdin.readline()

a, b = inp().split()

if int(a) > int(b):
    print(b, a)
else:
    print(a, b)