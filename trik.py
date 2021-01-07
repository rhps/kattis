#!/usr/bin/env python

"""
trik

https://open.kattis.com/problems/trik
"""

testcase = list(input())
pos = 1
for i in testcase:
    if i == "A":
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos = 1
        else:
            pass

    elif i == "B":
        if pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2
        else:
            pass

    elif i == "C":
        if pos == 1:
            pos = 3
        elif pos == 3:
            pos = 1
        else:
            pass
print(pos)