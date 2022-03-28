#!/usr/bin/env python

"""
GCVWR

https://open.kattis.com/problems/gcvwr
"""
import sys
def inp():
    return sys.stdin.readline()


g, t, n = inp().split()
rem = (int(g) - int(t))*0.9
w = inp().split()

for x in w:
    rem = rem - int(x)

print(int(rem))