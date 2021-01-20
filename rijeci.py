#!/usr/bin/env python

"""
Riječi

https://open.kattis.com/problems/rijeci
"""
import sys

cases = int(sys.stdin.readline())
A = 0
B = 1
for x in range(1,cases):
    C = B
    B = A + B
    A = C

print(A, B)