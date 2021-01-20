#!/usr/bin/env python

"""
Skocimis

https://open.kattis.com/problems/skocimis
"""
import sys
# sko = list(map(int, sys.stdin.readline().split()))

# moving = 0
# while True:
#     a,b,c = sko
#     ab = b - a
#     bc = c - b
#     if (ab > bc) and ab > 1:
#         c = a + 1
#     elif (ab < bc) and bc > 1:
#         a = c - 1
#     else:
#         break
#     moving = moving + 1
#     sko = sorted([a,b,c])

# print(moving)

a, b, c = map(int, sys.stdin.readline().split())
d = b - a - 1
e = c - b - 1

if d > e:
    print(d)
else:
    print(e)