#!/usr/bin/env python

"""
Reversed Binary Numbers

https://open.kattis.com/problems/reversebinary
"""

inp = int(input())
inp = "{0:b}".format(inp) #string format
inp = list(reversed(list(inp)))
print(int("".join(inp), 2))