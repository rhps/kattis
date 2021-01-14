#!/usr/bin/env python

"""
Bus Numbers

https://open.kattis.com/problems/busnumbers
"""
import sys

case = int(sys.stdin.readline())
cases = list(map(int, sys.stdin.readline().split()))
cases = sorted(cases)
chain = 0
printing = []
for x in range(case-1):
    if cases[x+1] - cases[x] == 1:
        if cases[x+2] - cases[x+1] == 1:
            chain = chain + 1
        else:
            chain = chain + 1
            printing.append(cases[x])
    else:
        if chain > 1:
            printing.pop()
            printing.append(str(cases[x-chain]) + "-" + str(cases[x]))
            chain = 0
        elif chain == 1:
            printing.append(cases[x])
        else:
            printing.append(cases[x])
            chain = 0
printing.append(cases[-1])
print(" ".join(map(str, printing)))