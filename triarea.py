#!/usr/bin/env python

"""
Triangle Area

https://open.kattis.com/problems/triarea
"""
import sys
def inp():
    return sys.stdin.readline()

a, b = inp().split()

print(int(a)*int(b)/2)