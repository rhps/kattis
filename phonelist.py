#!/usr/bin/env python

"""
Phone List

https://open.kattis.com/problems/phonelist
"""
import sys

for x in range(eval(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    phonenum = sorted([sys.stdin.readline()[:-1] for _ in range(n)], key=len, reverse=True)
    phonecheck = set()
    consistent = True

    for num in phonenum:
        if not consistent:
            continue
        if num in phonecheck:
            consistent = False
            continue
        for i in range(1, len(num)+1):
            phonecheck.add(num[:i])
    if consistent:
        print("YES")
    else:
        print("NO")