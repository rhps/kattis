#!/usr/bin/env python

"""
Pot

https://open.kattis.com/problems/pot
"""
res = 0
for i in range(int(input())):
    val = input()
    num = int(val[0:-1])
    pow = int(val[-1])
    res = res + num**pow

print(res)