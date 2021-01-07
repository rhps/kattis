#!/usr/bin/env python

"""
Filip

https://open.kattis.com/problems/filip
"""

a, b = input().split()
a = int("".join(list(reversed(a))))
b = int("".join(list(reversed(b))))

if a > b:
    print(a)
else:
    print(b)
