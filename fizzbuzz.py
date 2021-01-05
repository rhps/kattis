#!/usr/bin/env python

"""
FizzBuzz

https://open.kattis.com/problems/fizzbuzz
"""

x,y,n = input().split()
x = int(x)
y = int(y)
n = int(n)
for j in range(n):
    i = j + 1
    if ((i%x == 0) & (i%y == 0)):
        print("FizzBuzz")
    elif (i%x) == 0:
        print("Fizz")
    elif (i%y) == 0:
        print("Buzz")
    else:
        print(i)