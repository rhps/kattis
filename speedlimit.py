#!/usr/bin/env python

"""
Speed Limit

https://open.kattis.com/problems/speedlimit
"""

while True:
    testcase = int(input())

    if testcase == -1:
        break
    else:
        miles = 0
        timebefore = 0
        for x in range(testcase):
            spd, time = input().split()
            miles = miles + (int(spd) * (int(time) - timebefore))
            timebefore = int(time)
        print(str(miles) + " miles")