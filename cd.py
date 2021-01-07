#!/usr/bin/env python

"""
CD

https://open.kattis.com/problems/cd
"""

import sys

while True:
    m, n = map(int, sys.stdin.readline().split())

    if m == 0 and n == 0:
        break
    else:
        jack = set(int(sys.stdin.readline()) for _ in range(m))
        jill = set(int(sys.stdin.readline()) for _ in range(n))
        print(len(jack&jill))