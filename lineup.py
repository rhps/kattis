#!/usr/bin/env python

"""
Line Them Up

https://open.kattis.com/problems/lineup
"""
import sys
case = int(sys.stdin.readline())
word = []

for x in range(case):
    word.append(sys.stdin.readline())

if word == sorted(word, reverse=True):
    print("DECREASING")
elif word == sorted(word):
    print("INCREASING")
else:
    print("NEITHER")