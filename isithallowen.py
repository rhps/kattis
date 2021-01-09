#!/usr/bin/env python

"""
IsItHalloween.com

https://open.kattis.com/problems/isithalloween
"""
import sys

m, d = sys.stdin.readline().split()
m = str(m)
d = int(d)

if (m == "OCT" and d == 31) or (m == "DEC" and d == 25):
    print("yup")
else:
    print("nope")