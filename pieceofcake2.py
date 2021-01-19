#!/usr/bin/env python

"""
Piece of Cake!

https://open.kattis.com/problems/pieceofcake2
"""
import sys

n, v, h = map(int, sys.stdin.readline().split())

l = []
l.append(v*h*4)
l.append((n-v)*h*4)
l.append((n-v)*(n-h)*4)
l.append(v*(n-h)*4)
print(max(l))