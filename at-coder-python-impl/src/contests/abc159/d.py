# -*- coding:utf-8 -*-
"""
D - Banned K.
"""
__author__ = "09x3086"

N = int(input())
M = [int(x) for x in input().split()]

Answer = []
num = 0

while num < N:
    count = 0
    M1 = M[:]
    M1.pop(num)
    for i, j in enumerate(M1):
        for k, v in enumerate(M1):
            if k > i and j == v:
                count += 1
    print(count)
    num += 1


