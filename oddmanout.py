#!/usr/bin/env python

"""
Odd Man Out

https://open.kattis.com/problems/oddmanout
"""
import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    cntguess = int(sys.stdin.readline())
    guess = list(map(int, sys.stdin.readline().split()))
    for j in range(len(guess)):
        if guess.count(guess[j]) == 1:
            print("Case #" + str(i+1) + ": " + str(guess[j]))
        else:
            pass