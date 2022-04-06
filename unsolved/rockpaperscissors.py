#!/usr/bin/env python

"""
Rock-Paper-Scissors Tournament

https://open.kattis.com/problems/rockpaperscissors
"""
from cProfile import run
from copy import copy
from random import sample
import sys
from unittest import case
def inp():
    return sys.stdin.readline()

while True:
    runn = inp().split()
    if runn == ["0"]:
        break
    else:
        n, k = runn
        point = [0]*int(n)

        for x in range(int(int(k)*int(n)*(int(n)-1)/2)):
            p1, m1, p2, m2 = inp().split()
            
            if m1 == "paper" and m2 == "rock":
                point[int(p1)-1] = point[int(p1)-1] + 1
            elif m2 == "paper" and m1 == "rock":
                point[int(p2)-1] = point[int(p2)-1] + 1
            elif m1 == "scissors" and m2 == "paper":
                point[int(p1)-1] = point[int(p1)-1] + 1
            elif m2 == "scissors" and m1 == "paper":
                point[int(p2)-1] = point[int(p2)-1] + 1
            elif m1 == "rock" and m2 == "scissors":
                point[int(p1)-1] = point[int(p1)-1] + 1
            elif m2 == "rock" and m1 == "scissors":
                point[int(p2)-1] = point[int(p2)-1] + 1

        for x in range(int(n)):
            if sum(point) == 0:
                print("-")
                break
            else:
                print('{0:.{1}f}'.format(point[x]/sum(point), 3))