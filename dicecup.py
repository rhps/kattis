#!/usr/bin/env python

"""
Dice Cup

https://open.kattis.com/problems/dicecup
"""
import sys
m,n = map(int, sys.stdin.readline().split())

if m <= n:
    for x in range(m,n+1):
        print(x+1)
else:
    for x in range(n,m+1):
        print(x+1)