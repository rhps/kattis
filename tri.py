#!/usr/bin/env python

"""
Tri

https://open.kattis.com/problems/tri
"""

import sys

a, b, c = map(int, sys.stdin.readline().split())

if a + b == c:
    print(str(a)+"+"+str(b)+"="+str(c))
    sys.exit()

if a - b == c:
    print(str(a)+"-"+str(b)+"="+str(c))
    sys.exit()

if a * b == c:
    print(str(a)+"*"+str(b)+"="+str(c))
    sys.exit()

if a / b == c:
    print(str(a)+"/"+str(b)+"="+str(c))
    sys.exit()

if a == b + c:
    print(str(a)+"="+str(b)+"+"+str(c))
    sys.exit()

if a == b - c:
    print(str(a)+"="+str(b)+"-"+str(c))
    sys.exit()

if a == b * c:
    print(str(a)+"="+str(b)+"*"+str(c))
    sys.exit()

if a == b / c:
    print(str(a)+"="+str(b)+"/"+str(c))
    sys.exit()