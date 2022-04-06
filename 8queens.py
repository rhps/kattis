#!/usr/bin/env python

"""
Eight Queens

https://open.kattis.com/problems/8queens
"""
from copy import copy
from random import sample
import sys
def inp():
    return sys.stdin.readline()

def horizontal(j, checkrow):
    for k in range(8):
        if k == j:
            continue
        if checkrow[k] == '*':
            return False
    return True

def vertikal(allchess, j, k):
    for i in range(8):
        if i == j:
            continue
        if allchess[i][k] == '*':
            return False
    return True

def diagonal(allchess, j, k):
    # First Diagonal, keatas, kiri
    current_j = j
    current_k = k
    while True:
        current_j -= 1
        current_k -= 1
        if current_j < 0 or current_k < 0:
            break
        elif current_j == j and current_k == k:
            break
    
        if allchess[current_j][current_k] == '*':
            # print('found atas kiri', current_j+1, current_k+1)
            return False

    # Second Diagonal, kebawah, kanan
    current_j = j
    current_k = k
    while True:
        current_j += 1
        current_k += 1
        if current_j == j and current_k == k:
            break
        elif current_j > 7 or current_k > 7:
            break

        if allchess[current_j][current_k] == '*':
            # print('found bawah kanan,', current_j+1, current_k+1)
            return False

    # Third Diagonal, keatas, kanan
    current_j = j
    current_k = k
    while True:
        current_j -= 1
        current_k += 1
        if current_j == j and current_k == k:
            break
        elif current_j < 0 or current_k > 7:
            break

        if allchess[current_j][current_k] == '*':
            # print('found atas kanan,', current_j+1, current_k+1)
            return False
    
    # Forth Diagonal, kebawah, kiri
    current_j = j
    current_k = k
    while True:
        current_j += 1
        current_k -= 1
        if current_j == j and current_k == k:
            break
        elif current_j > 7 or current_k < 0:
            break

        if allchess[current_j][current_k] == '*':
            # print('found bawah kiri,', current_j+1, current_k+1)
            return False
    return True

chess = []
counter = 0
valid = True

for x in range(8):
    chess.append(list(inp())[:-1])

for x in range(8):
    for y in range(8):
        if chess[x][y] == '*':
            counter += 1
            # if not(diagonal(chess, x, y)):
            #     print(counter, 'break', x+1, y+1)
            if not(horizontal(y, chess[x]) and vertikal(chess, x, y) and diagonal(chess, x, y)):
                valid = False
                break
    if not valid:
        break

if valid and counter == 8:
    print("valid")
else:
    print("invalid")