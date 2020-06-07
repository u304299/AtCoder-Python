# -*- coding:utf-8 -*-
"""
E - Red and Green Apples.
"""
__author__ = "09x3086"

x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P = sorted(P, reverse=True)[:x]
Q = sorted(Q, reverse=True)[:y]
concat = P + Q + R
concat.sort(reverse=True)
print(sum(concat[:x + y]))
