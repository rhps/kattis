#!/usr/bin/env python

"""
No Duplicates

https://open.kattis.com/problems/nodup
"""
import sys

case = sys.stdin.readline().split()
setcase = set(case)

if len(case) == len(setcase):
    print("yes")
else:
    print("no")