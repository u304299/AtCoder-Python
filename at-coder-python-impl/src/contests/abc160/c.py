# -*- coding:utf-8 -*-
"""
C - Traveling Salesman around Lake.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

a = 0
for i in range(N[1] - 1):
    a = a + M[i + 1] - M[i]



print(a)
