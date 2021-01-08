#!/usr/bin/env python

"""
Grass Seed Inc.

https://open.kattis.com/problems/grassseed
"""
import sys
c = float(sys.stdin.readline())
l = int(sys.stdin.readline())

luas = 0.0000000
for i in range(l):
    wi, li = map(float, sys.stdin.readline().split())
    luas = luas + (wi*li)

print('{:.7f}'.format(luas*c))