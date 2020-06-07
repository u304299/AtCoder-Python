# -*- coding:utf-8 -*-
"""
B - Popular Vote.
"""
__author__ = "09x3086"

N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
A = sorted(A, reverse=True)[:M]

answer = "Yes"

for i in range(M):
    if A[i] < total / (4 * M):
        answer = "No"

print(answer)
