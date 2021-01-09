#!/usr/bin/env python

"""
Planting Trees

https://open.kattis.com/problems/plantingtrees
"""
import sys

cases = int(sys.stdin.readline())
caseocc = list(map(int, sys.stdin.readline().split()))
caseocc.sort(reverse=True)

newcaseocc = []

for i in range(len(caseocc)):
    newcaseocc.append(caseocc[i]+i+2)

print(max(newcaseocc))