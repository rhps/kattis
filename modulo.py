#!/usr/bin/env python

"""
Modulo

https://open.kattis.com/problems/modulo
"""
import sys
cnt = []

for x in range(10):
    inp = int(sys.stdin.readline()) % 42
    cnt.append(inp)
print(len(set(cnt)))