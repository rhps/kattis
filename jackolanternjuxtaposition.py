#!/usr/bin/env python

"""
Jack-O'-Lantern Juxtaposition

https://open.kattis.com/problems/jackolanternjuxtaposition
"""
import sys
def inp():
    return sys.stdin.readline()

a, b, c = inp().split()

print(int(a)*int(b)*int(c))