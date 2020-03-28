# -*- coding:utf-8 -*-
"""
E - Dividing Chocolate.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]
M = [input() for i in range(N[0])]

matrix = []
for i in M:
    L = []
    matrix.append(L)
    for j in i:
        L.append(j)

splitWidth = 1
splitHeight = 1
count = 0
A = 0
B = 0
C = 0
D = 0

while splitWidth < N[0]:
    for h, j in enumerate(matrix):
        for w, v in enumerate(j):
            if w < splitWidth and h < splitHeight:
                A = A + int(v)
            elif w >= splitWidth and h < splitHeight:
                B = B + int(v)
            elif w < splitWidth and h >= splitHeight:
                C = C + int(v)
            else:
                D = D + int(v)
    if A < N[2] and B < N[2] and C < N[2] and D < N[2]:
        break
    splitWidth = splitWidth + 1
    count = count + 1

print(count)
