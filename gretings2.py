#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

cases = list(inp())[:-1]

awal = []
akhir = []
e = 0
for x in cases:
    if x == "e":
        e = e + 1
    elif e == 0:
        awal.append(x)
    else:
        akhir.append(x)

print("".join(awal) + "".join(2*e*"e") + "".join(akhir))