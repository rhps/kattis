#!/usr/bin/env python

"""
Soylent

https://open.kattis.com/problems/soylent
"""
import sys, math

for x in range(int(sys.stdin.readline())):
    print(int(math.ceil(int(sys.stdin.readline())/400)))