#!/usr/bin/env python

"""
Pet

https://open.kattis.com/problems/pet
"""

tot = []
for i in range(5):
    a,b,c,d = input().split()
    tot.append(int(a)+int(b)+int(c)+int(d))


print(tot.index(max(tot))+1, max(tot))