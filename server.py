#!/usr/bin/env python

"""
Server

https://open.kattis.com/problems/server
"""
import sys

n, t = map(int, sys.stdin.readline().split())
case = list(map(int, sys.stdin.readline().split()))

def count(inp, t):
    tot = 0
    for i, x in enumerate(case):
        if x + tot > t:
            return(i)
        tot += x
    return len(case)

print(count(case, t))