#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()


day = { 5: "Monday", 
        6: "Tuesday", 
        0: "Wednesday",
        1: "Thursday",
        2: "Friday", 
        3: "Saturday",
        4: "Sunday"}

month = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
         11: 30,
         12: 31}

d, m = map(int, inp().split())
daytot = d

for x in range(1, m):
    daytot = daytot + month[x]

print(day[daytot%7])