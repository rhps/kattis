#!/usr/bin/env python

"""
The Easiest Problem Is This One

https://open.kattis.com/problems/easiest
"""
import sys

while True:
    case = int(sys.stdin.readline())

    if case == 0:
        break
    else:
        totcase = sum(map(int, list(str(case))))
        x = 11
        while True:
            rslt = sum(map(int, list(str(case * x))))
            if rslt == totcase:
                print(x)
                break
            else:
                x = x + 1