#!/usr/bin/env python

"""
Aaah!

https://open.kattis.com/problems/aaah
"""

sp1 = input().replace("h", "")
sp2 = input().replace("h", "")

if len(sp1) >= len(sp2):
    print("go")
else:
    print("no")