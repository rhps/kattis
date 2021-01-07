#!/usr/bin/env python

"""
Apaxiaaaaaaaaaaaans!

https://open.kattis.com/problems/apaxiaaans
"""

case = list(input())
outp = [case[0]]

for x in range(1, len(case)):
    if case[x] == case[x-1]:
        pass
    else:
        outp.append(case[x])

print("".join(outp))