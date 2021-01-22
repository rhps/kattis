#!/usr/bin/env python

"""
Final Exam

https://open.kattis.com/problems/finalexam2
"""
import sys
def inp():
    return sys.stdin.readline()


cases = int(inp())
prev = inp()
tot = 0
for x in range(cases-1):
    cur = inp()
    if prev == cur:
        tot = tot + 1
    prev = cur
print(tot)