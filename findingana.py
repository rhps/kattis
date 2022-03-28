#!/usr/bin/env python

"""
Finding An A

https://open.kattis.com/problems/findingana
"""
from copy import copy
import sys
def inp():
    return sys.stdin.readline()

s = list(inp())[:-1]
t = copy(s)

for x in range(len(s)):
    if s[x] == 'a':
        break
    else:
        t.pop(0)

print(''.join(t))