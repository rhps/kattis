#!/usr/bin/env python

"""
One Chicken Per Person!

https://open.kattis.com/problems/onechicken
"""
import sys

p, c = map(int, sys.stdin.readline().split())

if p > c:
    if p - c == 1:
        print("Dr. Chaz needs " + str(p-c) + " more piece of chicken!")
    else:
        print("Dr. Chaz needs " + str(p-c) + " more pieces of chicken!")
else:
    if c - p == 1:
        print("Dr. Chaz will have " + str(c-p) + " piece of chicken left over!")
    else:
        print("Dr. Chaz will have " + str(c-p) + " pieces of chicken left over!")