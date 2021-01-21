#!/usr/bin/env python

"""
Railroad

https://open.kattis.com/problems/railroad2
"""
import sys
def inp():
    return sys.stdin.readline()

x,y = map(int, inp().split())

tot = (4*x) + (3*y)

if tot%2 == 0:
    print("possible")
else:
    print("impossible")