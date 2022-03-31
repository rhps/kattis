#!/usr/bin/env python

"""
Count the Vowels

https://open.kattis.com/problems/countthevowels
"""
from copy import copy
import sys
def inp():
    return sys.stdin.readline()

samples = []

for y in range(5):
    psgr = list(inp())[:-1]
    x = 0
    for x in range(len(psgr)):
        if psgr[x] == 'F' and psgr[x+1] == 'B' and psgr[x+2]:
            samples.append(y+1)

if len(samples) > 0:
    print(" ".join(map(str, samples)))
else:
    print("HE GOT AWAY!")