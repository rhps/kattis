#!/usr/bin/env python

"""

"""
import sys
def inp():
    return sys.stdin.readline()

import math

while True:
    r, m, c = inp().split()
    if r == "0":
        break
    else:
        m = int(m)
        c = int(c)
        r = float(r)
        print('{:.9f}'.format(math.pi*r*r) + " " + str((c/m)*(4*r*r)))