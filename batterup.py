#!/usr/bin/env python

"""
Batter Up

https://open.kattis.com/problems/batterup
"""
import sys

cases = int(sys.stdin.readline())
occ = list(map(int, sys.stdin.readline().split()))
occ = [i for i in occ if i != -1]

print(sum(occ)/len(occ))