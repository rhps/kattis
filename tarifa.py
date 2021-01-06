#!/usr/bin/env python

"""
Tarifa

https://open.kattis.com/problems/tarifa
"""

x = input()
n = input()

tot = 0
for i in range(int(n)):
    j = input()
    tot = tot + int(x) - int(j)

print(tot+int(x))