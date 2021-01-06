#!/usr/bin/env python

"""
A Different Problem

https://open.kattis.com/problems/different
"""

while(True):
    try:
        inp = input()
    except EOFError:
        break
    a,b = inp.split()
    print(abs(int(a)-int(b)))