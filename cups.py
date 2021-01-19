#!/usr/bin/env python

"""
Stacking Cups

https://open.kattis.com/problems/cups
"""
import sys

cases = int(sys.stdin.readline())
mappingcolor = {}

for x in range(cases):
    case = sys.stdin.readline().split()

    if str.isdigit(case[0]):
        mappingcolor[int(int(case[0])/2)] = case[1]
    else:
        mappingcolor[int(case[1])] = case[0]

for x in sorted(mappingcolor.keys()):
    print(mappingcolor[x])