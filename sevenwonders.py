#!/usr/bin/env python

"""
Seven Wonders

https://open.kattis.com/problems/sevenwonders
"""

import sys

card = list(sys.stdin.readline())

t = 0
c = 0
g = 0
for x in card:
    if x == "T":
        t = t + 1
    elif x == "C":
        c = c + 1
    elif x == "G":
        g = g + 1
    else:
        pass

bonus = [t, c, g]

print(pow(t,2)+pow(c,2)+pow(g,2) + min(bonus)*7)