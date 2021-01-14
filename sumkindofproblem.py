#!/usr/bin/env python

"""
Sum Kind of Problem

https://open.kattis.com/problems/sumkindofproblem
"""
import sys

for x in range(eval(sys.stdin.readline())):
    l, n = map(int, sys.stdin.readline().split())
    s1, s1sum = 0, 0
    s2, s2sum = 0, 0
    s3, s3sum = 0, 0

    i = 1
    while s1 < n:
        s1 = s1 + 1
        s1sum = s1sum + i
        i = i + 1

    j = 1
    while s2 < n:
        if (j%2 == 0):
            s2 = s2 + 1
            s2sum = s2sum + j
        j = j + 1

    k = 1
    while s3 < n:
        if (k%2 == 1):
            s3 = s3 + 1
            s3sum = s3sum + k
        k = k + 1

    print(l, s1sum, s3sum, s2sum)