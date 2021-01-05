#!/usr/bin/env python

"""
Oddities

https://open.kattis.com/problems/oddities
"""

n = input()

for x in range(int(n)):
    m = input()
    if int(m)%2 == 0:
        print(m + " is even")
    else:
        print(m + " is odd")