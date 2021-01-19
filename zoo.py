#!/usr/bin/env python

"""
Un-bear-able Zoo

https://open.kattis.com/problems/zoo
"""
import sys
trying = 1

while True:
    cases = int(sys.stdin.readline())

    if cases == 0:
        break
    else:
        animal = {}
        for x in range(cases):
            case = list(sys.stdin.readline().split())[-1].lower()
            if case not in animal:
                animal[case] = 1
            else:
                animal[case] = animal[case] + 1

        print("List " + str(trying) + ":")
        for y in sorted(animal):
            print(y + " | " + str(animal[y]))
        trying = trying + 1