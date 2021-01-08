#!/usr/bin/env python

"""
Mixed Fractions

https://open.kattis.com/problems/mixedfractions
"""
import sys

while True:
    numerator, denominator = map(int, sys.stdin.readline().split())

    if numerator == 0 and denominator == 0:
        break
    else:
        print(str(numerator//denominator) + " " + str(numerator%denominator) + " / " + str(denominator))