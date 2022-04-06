#!/usr/bin/env python

"""
T9 Spelling

https://open.kattis.com/problems/t9spelling
"""
from copy import copy
from random import sample
import sys
from unittest import case
def inp():
    return sys.stdin.readline()

N = int(inp())

keymap = [  "",     "abc", "def", 
            "ghi",  "jkl", "mno", 
            "pqrs", "tuv", "wxyz", " "]

for x in range(N):
    cnt = 0
    chars = list(inp())[:-1]
    cur = []
    for y in range(len(chars)):
        for z in range(10):
            for a in range(len(keymap[z])):
                if chars[y] == keymap[z][a]:
                    if len(cur) >= 1:
                        if (int(cur[-1][-1]) == int(z+1)) or (int(cur[-1][-1]) == 0 and int(z) == 9):
                            cur.append(" ")
                    if z == 9:
                        cur.append(str(0)*(a+1))
                    else:
                        cur.append(str(z+1)*(a+1))
    print("Case #" + str(x+1) + ": " + "".join(cur))