#!/usr/bin/env python

"""
Skener

https://open.kattis.com/problems/skener
"""
import sys
r, c, zr, zc = map(int, sys.stdin.readline().split())

mapp = []
for x in range(r):
    mapr = list(sys.stdin.readline())[:-1]
    mapp.append(mapr)

for i in range(0,r*zr):
    printout = []
    for j in range(0, c*zc):
        printout.append(mapp[int(i/zr)][int(j/zc)])
    print("".join(printout))