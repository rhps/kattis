#!/usr/bin/env python

"""
10 Kinds of People

https://open.kattis.com/problems/10kindsofpeople
"""
import sys

x,y = map(int, sys.stdin.readline().split())

coordinate = []
for i in range(x):
    coordinatey = list(sys.stdin.readline()[:-1])
    coordinate.append(coordinatey)

testcase = int(sys.stdin.readline())

for j in range(testcase):
    case = list(map(int, sys.stdin.readline().split()))

    print(coordinate[case[0]-1][case[1]-1], coordinate[case[2]-1][case[3]-1])
