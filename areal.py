#!/usr/bin/env python

"""
A Real Challenge

https://open.kattis.com/problems/areal
"""
import sys, math
area = int(sys.stdin.readline())

pagar = 4*math.sqrt(area)
print("{:6f}".format(pagar))