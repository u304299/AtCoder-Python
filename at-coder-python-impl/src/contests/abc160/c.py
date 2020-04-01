# -*- coding:utf-8 -*-
"""
C - Traveling Salesman around Lake.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

a = 0
for i in range(N[1] - 1):
    if abs(M[i + 1] - N[0] / 2) - M[i] >= N[0] / 2:
        a = a + abs(M[i + 1] - N[0])
    else:
        a = a + M[i + 1] - M[i]

print(a)
