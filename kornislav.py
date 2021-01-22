#!/usr/bin/env python

"""
Kornislav

https://open.kattis.com/problems/kornislav
"""
import sys
def inp():
    return sys.stdin.readline()

length = sorted(list(map(int, inp().split())))

print(length[0]*length[2])