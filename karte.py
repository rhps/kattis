#!/usr/bin/env python

"""
Karte

https://open.kattis.com/problems/karte
"""
import sys
def inp():
    return sys.stdin.readline()

cases = list(inp())

P = []
K = []
H = []
T = []
for x in range(len(cases)):
    if x % 3 == 0:
        if cases[x] == "P":
            P.append("P"+cases[x+1]+cases[x+2])
        if cases[x] == "K":
            K.append("K"+cases[x+1]+cases[x+2])
        if cases[x] == "H":
            H.append("H"+cases[x+1]+cases[x+2])
        if cases[x] == "T":
            T.append("T"+cases[x+1]+cases[x+2])

if len(P) != len(set(P)) or len(K) != len(set(K)) or len(H) != len(set(H)) or len(T) != len(set(T)):
    print("GRESKA")
else:
    print(13-len(P), 13-len(K), 13-len(H), 13-len(T))