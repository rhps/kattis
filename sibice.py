#!/usr/bin/env python

"""
Sibice

https://open.kattis.com/problems/sibice
"""
import math
case, a, b = input().split()

c = math.sqrt(int(a)**2 + int(b)**2)

for x in range(int(case)):
    y = int(input())
    if y > c:
        print("NE")
    else:
        print("DA")