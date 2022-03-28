#!/usr/bin/env python

"""
Odd Echo

https://open.kattis.com/problems/oddecho
"""
import sys
def inp():
    return sys.stdin.readline()

n = int(inp())

for x in range(n):
    xi = inp()[:-1]
    if x%2 == 0:
        print(xi)
