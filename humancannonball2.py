#!/usr/bin/env python

"""
The Amazing Human Cannonball

https://open.kattis.com/problems/humancannonball2
"""
import sys, math
cases = int(sys.stdin.readline())

def y(v0, theta, t):
    return (v0*t*math.sin(math.radians(theta)) - (0.5*9.81*t*t))

def time(x1, v0, theta):
    return (x1/(v0*math.cos(math.radians(theta))))

for x in range(cases):
    v0, theta, x1, h1, h2 = map(float, sys.stdin.readline().split())

    t = time(x1, v0, theta)
    ycal = y(v0, theta, t)

    if (ycal > (h1 + 1)) and (ycal < (h2 -1)):
        print("Safe")
    else:
        print("Not Safe")