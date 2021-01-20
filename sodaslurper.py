#!/usr/bin/env python

"""
Soda Slurper

https://open.kattis.com/problems/sodaslurper
"""
import sys

e, f, c = map(int, sys.stdin.readline().split())

soda = 0
n = e + f
while n >= c:
    n = n - c + 1
    soda = soda + 1

print(soda)