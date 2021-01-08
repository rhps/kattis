#!/usr/bin/env python

"""
Quick Estimates

https://open.kattis.com/problems/quickestimate
"""
import sys

cases = int(sys.stdin.readline())

for x in range(cases):
    y = str(sys.stdin.readline())
    print(len(y)-1)