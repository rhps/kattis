#!/usr/bin/env python

"""
Last Factorial Digit

https://open.kattis.com/problems/lastfactorialdigit
"""

import math, sys

cases = int(sys.stdin.readline())

for x in range(cases):
    case = int(sys.stdin.readline())
    print(str(math.factorial(case))[-1])