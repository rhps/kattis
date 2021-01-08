#!/usr/bin/env python

"""
Cryptographer's Conundrum

https://open.kattis.com/problems/conundrum
"""

import sys

txt = sys.stdin.readline()
cnt = 0

for i in range(1, len(txt)):
    if i%3 == 0:
        if txt[i-1] != "R":
            cnt = cnt + 1
    elif i%3 == 1:
        if txt[i-1] != "P":
            cnt = cnt + 1
    elif i%3 == 2:
        if txt[i-1] != "E":
            cnt = cnt + 1
    else:
        pass

print(cnt)