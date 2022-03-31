#!/usr/bin/env python

"""
Count the Vowels

https://open.kattis.com/problems/countthevowels
"""
from copy import copy
import sys
def inp():
    return sys.stdin.readline()

s = list(inp())[:-1]
cnt = 0
for x in s:
    if x.capitalize() in ['A', 'I', 'U', 'E', 'O']:
        cnt = cnt + 1

print(cnt)