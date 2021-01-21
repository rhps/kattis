#!/usr/bin/env python

"""
Pizza Crust

https://open.kattis.com/problems/pizza2
"""
import sys
def inp():
    return sys.stdin.readline()

r, c = map(float, inp().split())

print('{:.6f}'.format((r-c)*(r-c)/(r*r)*100))