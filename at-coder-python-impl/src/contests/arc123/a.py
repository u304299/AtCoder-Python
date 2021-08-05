# -*- coding:utf-8 -*-
"""
D - Banned K.
"""
__author__ = "09x3086"

N = [int(x) for x in input().split()]

Answer = []
num = 0
count = 0

if N[1] - N[0] == 0:
    count = abs(N[1] - N[2])
if N[2] - N[1] == 0:
    count = abs(N[1] - N[0])
if N[2] - N[0] == 0:
    count = abs(N[1] - N[0])
else:
    while N[1] - N[0] != N[2] - N[1]:
        count += 1
        if N[1] - N[0] > N[2] - N[1]:
            N[2] += 1
        if N[1] - N[0] < N[2] - N[1]:
            N[1] += 1

print(count)
