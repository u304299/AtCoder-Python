# -*- coding:utf-8 -*-
"""
C - Traveling Salesman around Lake.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

distanceList = []

distance = 0
for i in range(N[1]):
    M.append((M[i] + N[0]))

for i in range(len(M) - 1):
    distanceList.append(M[i + 1] - M[i])

print(distanceList)
print(N[0] - max(distanceList))
