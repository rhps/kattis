#!/usr/bin/env python

"""
Stand on Zanzibar

https://open.kattis.com/problems/zanzibar
"""
import sys

cases = int(sys.stdin.readline())

for x in range(cases):
    pop = list(map(int, sys.stdin.readline().split()))[:-1]
    tot = 0

    for x in range(1, len(pop)):
        migrate = pop[x] - (2*pop[x-1])
        if migrate < 0:
            migrate = 0
        tot = tot + migrate
    
    print(tot)