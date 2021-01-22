#!/usr/bin/env python

"""
Mirror Images

https://open.kattis.com/problems/mirror
"""
import sys
def inp():
    return sys.stdin.readline()

for n in range(int(inp())):
    x,y = map(int, inp().split())
    matrix = []
    for y in range(x):
        matrix.append(list(reversed(list(inp())[:-1])))

    matrix = list(reversed(matrix))
    print("Test " + str(n+1))

    for z in range(x):
        print("".join(matrix[z]))