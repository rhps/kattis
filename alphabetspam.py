#!/usr/bin/env python

"""
Alphabet Spam

https://open.kattis.com/problems/alphabetspam
"""
import sys

case = list(sys.stdin.readline()[:-1])

space = 0
lower = 0
upper = 0
ln = len(case)

for x in case:
    if x.islower():
        lower = lower + 1
    else:
        pass

    if x.isupper():
        upper = upper + 1
    else:
        pass

    if x.isspace() or x == "_":
        space = space + 1
    else:
        pass

print('{:.15f}'.format(space/ln))
print('{:.15f}'.format(lower/ln))
print('{:.15f}'.format(upper/ln))
print('{:.15f}'.format((ln-space-lower-upper)/ln))