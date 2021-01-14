#!/usr/bin/env python

"""
Heart Rate
https://open.kattis.com/problems/heartrate
"""
import sys

case = int(sys.stdin.readline())

for x in range(case):
    b, p = sys.stdin.readline().split()
    b = int(b)
    p = float(p)
    bpm = 60*b/p
    abpm = 60/(p)

    print("{:.4f}".format(bpm - abpm), "{:.4f}".format(bpm), "{:.4f}".format(bpm + abpm))