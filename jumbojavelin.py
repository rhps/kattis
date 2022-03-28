#!/usr/bin/env python

"""
Jumbo Javelin

https://open.kattis.com/problems/jumbojavelin
"""
import sys
def inp():
    return sys.stdin.readline()

n = int(inp())
tot = 0

for x in range(n):
    tot = tot + int(inp())

print(tot-n+1)