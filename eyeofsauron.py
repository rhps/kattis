#!/usr/bin/env python

"""
Eye of Sauron

https://open.kattis.com/problems/eyeofsauron
"""
from copy import copy
import sys
def inp():
    return sys.stdin.readline()

n = list(inp())[:-1]
m = copy(n)

for x in range(len(n)):
    if n[x] == '(':
        break
    else:
        m.pop(0)

if len(m)-1 == len(n)/2:
    print("correct")
else:
    print("fix")