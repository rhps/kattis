#!/usr/bin/env python

"""
Shattered Cake

https://open.kattis.com/problems/shatteredcake
"""
import sys
def inp():
    return sys.stdin.readline()

w = int(inp())
n = int(inp())
l = 0
for x in range(n):
    a, b = inp().split()
    l = l + (int(a)*int(b))

print(int(l/w))