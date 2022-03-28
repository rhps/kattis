#!/usr/bin/env python

"""
Rating Problems

https://open.kattis.com/problems/ratingproblems
"""
import sys
def inp():
    return sys.stdin.readline()

n, k = inp().split()
tot = 0

for x in range(int(k)):
    y = int(inp())
    tot = tot + y

print(((tot+(-3*(int(n)-int(k))))/int(n)), ((tot+(3*(int(n)-int(k))))/int(n)))