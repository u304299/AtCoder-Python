# -*- coding:utf-8 -*-
"""
C - Replacing Integer.
"""
__author__ = "09x3086"

N, K = map(int, input().split())

answer = N % K
x = K - answer

if answer > x:
    answer = x

print(answer)
