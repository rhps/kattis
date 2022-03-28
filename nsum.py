#!/usr/bin/env python

"""
N-sum

https://open.kattis.com/problems/nsum
"""
import sys
def inp():
    return sys.stdin.readline()

n = int(inp())

tot = 0
x = inp().split()

for i in range(n):
    tot = tot + int(x[i])

print(tot)