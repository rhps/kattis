#!/usr/bin/env python

"""
Quick Brown Fox

https://open.kattis.com/problems/quickbrownfox
"""

import sys

cases = int(sys.stdin.readline())
tst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x in range(cases):
    pangram = []
    case = str(sys.stdin.readline())
    
    for y in tst:
        if y in (case.lower()):
            pass
        else:
            pangram.append(y)
    
    if len(pangram) == 0:
        print('pangram')
    else:
        print("missing " + "".join(pangram))