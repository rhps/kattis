#!/usr/bin/env python

"""
Symmetric Order

https://open.kattis.com/problems/symmetricorder
"""
import sys,math

i = 1
while True:
    case = int(sys.stdin.readline())

    if case == 0:
        break
    else:
        sets = []
        for x in range(case):
            sets.append(sys.stdin.readline()[:-1])
        
        sets = sorted(sets, key=len)
        newsets = []

        print("SET " + str(i))
        for y in range(0, case, 2):
            print(sets[y])
            if y < case-1:
                newsets.append(sets[y+1])

        newsets = reversed(newsets)
        for z in newsets:
            print(z)
        i = i + 1