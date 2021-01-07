#!/usr/bin/env python

"""
Ladder

https://open.kattis.com/problems/ladder
"""
import sys, math

d, teta = map(int, sys.stdin.readline().split())

print(math.ceil(d/math.sin(math.radians(teta))))