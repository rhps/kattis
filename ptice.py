#!/usr/bin/env python

"""
Ptice

https://open.kattis.com/problems/ptice
"""
import sys
def inp():
    return sys.stdin.readline()

cases = int(inp())
case = list(inp()[:-1])

adrian = ['A','B','C']
bruno = ['B','A','B','C']
goran = ['C','C','A','A','B','B']

adrianscore = 0
brunoscore = 0
goranscore = 0

for x in range(cases):
    if case[x] == adrian[x%3]:
        adrianscore = adrianscore + 1

    if case[x] == bruno[x%4]:
        brunoscore = brunoscore + 1

    if case[x] == goran[x%6]:
        goranscore = goranscore + 1

score = {   'Adrian' : adrianscore,
            'Bruno' : brunoscore,
            'Goran' : goranscore}

maks = max((score.values()))
print(maks)

for key, val in score.items():
    if val == maks:
        print(key)