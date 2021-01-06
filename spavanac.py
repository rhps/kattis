#!/usr/bin/env python

"""
Spavanac

https://open.kattis.com/problems/spavanac
"""

h,m = input().split()
h = int(h)
m = int(m)

if m>=45:
    mrest=m-45
    print(h, mrest)
else:
    if h==0:
        mrest=60+m-45
        print(h+24-1, mrest)
    else:
        mrest=60+m-45
        print(h-1, mrest)