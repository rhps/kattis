#!/usr/bin/env python

"""
Babelfish

https://open.kattis.com/problems/babelfish
"""
import sys

dict = {}
while True:
    inp = sys.stdin.readline()
    if inp == "\n":
        break
    else:
        ref, ky = inp.split()
        dict[ky] = ref

while True:
    inp = sys.stdin.readline()[:-1]
    if inp == "":
        break
    else:
        if inp in dict:
            print(dict[inp])
        else:
            print("eh")
