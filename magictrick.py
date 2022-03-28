#!/usr/bin/env python

"""
Magic Trick

https://open.kattis.com/problems/magictrick
"""
import sys
def inp():
    return sys.stdin.readline()

s = list(inp())[:-1]

if len(s) == len(set(s)):
    print(1)
else:
    print(0)