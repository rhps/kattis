#!/usr/bin/env python

"""
Judging Moose

https://open.kattis.com/problems/judgingmoose
"""
import sys

l, r = map(int, sys.stdin.readline().split())

if (l == 0) and (r == 0):
    print("Not a moose")
elif (l == r):
    print("Even " + str(l*2))
elif (l < r):
    print("Odd "+ str(r*2))
elif (l > r):
    print("Odd "+ str(l*2))
else:
    pass