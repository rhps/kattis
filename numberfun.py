#!/usr/bin/env python

"""
Number Fun

https://open.kattis.com/problems/numberfun
"""
import sys

case = int(sys.stdin.readline())

for x in range(case):
    a, b, c = map(int, sys.stdin.readline().split())

    possible = False

    if (a + b) == c:
        possible = True
    elif (a - b) == c:
        possible = True
    elif (a * b) == c:
        possible = True
    elif (a / b) == c:
        possible = True
    elif (c + b) == a:
        possible = True
    elif (c - b) == a:
        possible = True
    elif (c * b) == a:
        possible = True
    elif (c / b) == a:
        possible = True
    elif (a + c) == b:
        possible = True
    elif (a - c) == b:
        possible = True
    elif (a * c) == b:
        possible = True
    elif (a / c) == b:
        possible = True
    elif (b - a) == c:
        possible = True
    elif (b / a) == c:
        possible = True
    elif (b - c) == a:
        possible = True
    elif (b / c) == a:
        possible = True
    elif (c - a) == b:
        possible = True
    elif (c / a) == b:
        possible = True
    else:
        pass

    if possible:
        print("Possible")
    else:
        print("Impossible")