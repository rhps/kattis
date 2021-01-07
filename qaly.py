#!/usr/bin/env python

"""
Quality-Adjusted Life-Year

https://open.kattis.com/problems/qaly
"""

case = input()

outp = 0.0
for x in range(int(case)):
    a, b = input().split()
    outp = outp + (float(a) * float(b))

print("{:.3f}".format(outp))