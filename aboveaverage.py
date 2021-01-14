#!/usr/bin/env python

"""
Above Average

https://open.kattis.com/problems/aboveaverage
"""
import sys, math

case = int(sys.stdin.readline())

for x in range(case):
    inp = list(map(int, sys.stdin.readline().split()))
    inp.remove(inp[0])
    avrg = [y for y in inp if y > (sum(inp)/len(inp))]
    print("{:.3f}%".format(len(avrg)*100/len(inp)))