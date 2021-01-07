#!/usr/bin/env python

"""
Cold-puter Science

https://open.kattis.com/problems/cold
"""

case = int(input())
temp = input().split()

worstday = 0
for x in range(len(temp)):
    if int(temp[x]) < 0:
        worstday = worstday + 1

print(worstday)