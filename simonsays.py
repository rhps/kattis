#!/usr/bin/env python

"""
Simon Says

https://open.kattis.com/problems/simonsays
"""
import sys

case = int(sys.stdin.readline())

for x in range(case):
    testcase = sys.stdin.readline()

    if "Simon says " in testcase:
        print(testcase.replace("Simon says ", ""))