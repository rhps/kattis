#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

maks, events = map(int, inp().split())
people = 0
denied = 0

for x in range(events):
    event, tot = inp().split()
    if event == 'enter':
        if people + int(tot) <= maks:
            people = people + int(tot)
        else:
            denied = denied + 1
    else:
        people = people - int(tot)
print(denied)