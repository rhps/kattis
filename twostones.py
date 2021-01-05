#!/usr/bin/env python

"""
Take Two Stones

https://open.kattis.com/problems/twostones
"""

stone = input()

if int(stone)%2 == 0:
    print("Bob")
else:
    print("Alice")