#!/usr/bin/env python

"""
Cetvrta

https://open.kattis.com/problems/cetvrta
"""
import sys

x = []
y = []

for i in range(3):
    xi, yi = map(int, sys.stdin.readline().split())
    x.append(xi)
    y.append(yi)
xx = 0
yy = 0

for i in range(3):
    if x.count(x[i]) == 1:
        xx = x[i]
    else:
        pass
    if y.count(y[i]) == 1:
        yy = y[i]
    else:
        pass

print(xx, yy)