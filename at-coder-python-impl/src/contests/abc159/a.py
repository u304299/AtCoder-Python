# -*- coding:utf-8 -*-
"""
A - The Number of Even Pairs.
"""
__author__ = "09x3086"

N, M = (int(x) for x in input().split())
myList = []
num = 0
while num < N:
    myList.append(2)
    num += 1

num = 0
while num < M:
    myList.append(1)
    num += 1

count = 0
num = 0
for i, j in enumerate(myList):
    for k, v in enumerate(myList):
        if k > i and (j + v) % 2 == 0:
            count += 1
print(count)
