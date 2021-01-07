#!/usr/bin/env python

"""
Nasty Hacks

https://open.kattis.com/problems/nastyhacks
"""

case = int(input())

for x in range(case):
    r, e ,c  = input().split()

    if int(e) - int (c) > int(r):
        print("advertise")
    elif int(e) - int (c) == int(r):
        print("does not matter")
    else:
        print("do not advertise")