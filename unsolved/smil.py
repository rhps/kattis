#!/usr/bin/env python

"""
SMIL

https://open.kattis.com/problems/smil
"""
from copy import copy
from random import sample
import sys
def inp():
    return sys.stdin.readline()

n = list(inp())[:-1]
samples = []
for x in range(len(n)):
    if n[x] == ':' and (len(n) - 2) > x and (n[x-1] == '-' and n[x-2] == ')'):
        samples.append(x)
        print(x)
    elif n[x] == ';' and (len(n)-2) > x and (n[x-1] == '-' and n[x-2] == ')'):
        samples.append(x)
        print(x)
    
print(samples)