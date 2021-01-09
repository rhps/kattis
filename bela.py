#!/usr/bin/env python

"""
Bela

https://open.kattis.com/problems/bela
"""
import sys

N, B = sys.stdin.readline().split()
N = int(N)
B = str(B)

dominant = {"A": 11, "K": 4, "Q":3,
            "J": 20, "T": 10, "9": 14,
            "8": 0, "7": 0}
notdominant = {"A": 11, "K": 4, "Q":3,
            "J": 2, "T": 10, "9": 0,
            "8": 0, "7": 0}
tot = 0

for x in range(4*N):
    a,b = list(str(sys.stdin.readline())[:-1])
    if b == B:
        tot = tot + dominant[a]
    else:
        tot = tot + notdominant[a]
    
print(tot)