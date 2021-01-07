#!/usr/bin/env python

"""
I've Been Everywhere, Man

https://open.kattis.com/problems/everywhere
"""

testcase = int(input())

for x in range(testcase):
    city = []
    travel = int(input())

    for y in range(travel):
        city.append(input())
    print(len(set(city)))