#!/usr/bin/env python

"""
Autori

https://open.kattis.com/problems/autori
"""

names = input().split("-")

singkatan = ""

for x in names:
    singkatan = singkatan + x[0]

print(singkatan)