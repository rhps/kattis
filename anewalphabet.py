#!/usr/bin/env python

"""
A New Alphabet

https://open.kattis.com/problems/anewalphabet
"""
import sys

new = {"a":"@", "b":"8", "c": "(", "d":"|)", "e":"3","f":"#","g":"6",
    "h":"[-]","i":"|","j":"_|","k":"|<","l":"1","m":"[]\/[]",
    "n":"[]\[]","o":"0","p":"|D","q":"(,)","r":"|Z","s":"$",
    "t":"']['","u":"|_|","v":"\/","w":"\/\/","x":"}{","y":"`/",
    "z":"2"}
case = sys.stdin.readline()

out = ""
for x in case.lower():
    if x in new:
        out = out + new[x]
    else:
        out = out + x

print(out)