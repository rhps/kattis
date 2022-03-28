#!/usr/bin/env python

"""
Job Expenses

https://open.kattis.com/problems/jobexpenses
"""
import sys
def inp():
    return sys.stdin.readline()

n = int(inp())
k = inp().split()
tot = 0

for x in k:
    if int(x) < 0:
        tot = tot + abs(int(x))

print(tot)