#!/usr/bin/env python

"""
Zamka

https://open.kattis.com/problems/zamka
"""
import sys

l = int(sys.stdin.readline())
d = int(sys.stdin.readline())
x = int(sys.stdin.readline())

lxd = []
for i in range(l, d+1):
    if int(sum(map(int, list(str(i))))) == x:
        lxd.append(i)

print(min(lxd))
print(max(lxd))