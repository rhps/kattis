#!/usr/bin/env python

"""
Detailed Differences

https://open.kattis.com/problems/detaileddifferences
"""
import sys

case = int(sys.stdin.readline())

for x in range(case):
    pair1 = str(sys.stdin.readline())[:-1]
    pair2 = str(sys.stdin.readline())
    outp = []
    for y in range(len(pair1)):
        if pair1[y] == pair2[y]:
            outp.append(".")
        else:
            outp.append("*")

    print(pair1, end='\n')
    print(pair2, end='\n')
    print("".join(outp), end='\n')