#!/usr/bin/env python

"""
FYI

https://open.kattis.com/problems/fyi
"""
import sys
def inp():
    return sys.stdin.readline()

n = list(inp())[:-1]

if (n[0:3] == ['5','5','5']) and (len(n) == 7):
    print(1)
else:
    print(0)