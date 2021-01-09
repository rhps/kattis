#!/usr/bin/env python

"""
Sort of Sorting

https://open.kattis.com/problems/sortofsorting
"""
import sys

while True:
    case = int(sys.stdin.readline())

    if case == 0:
        break
    else:
        names = []
        for x in range(case):
            inp = str(sys.stdin.readline())[:-1]
            names.append(inp)
        
        for y in sorted(names, key=lambda x: x[0:2]):
            print(y)