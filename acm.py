#!/usr/bin/env python

"""
ACM Contest Scoring

https://open.kattis.com/problems/acm
"""
import sys

tot = 0
allansw = []
rightansw = []
while True:
    inp = sys.stdin.readline()[:-1]
    if inp == "-1":
        break
    else:
        min, prblm, answ = inp.split()
        min = int(min)

        if answ == "right" and prblm not in rightansw:
            tot = tot + min
            rightansw.append(prblm)
            for j in allansw:
                if (j[1] == prblm):
                    tot = tot + 20
                else:
                    pass
        else:
            pass
        # print(tot)
        allansw.append([min, prblm, answ])
    
print(len(rightansw) ,tot)