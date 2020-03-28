# -*- coding:utf-8 -*-
"""
B - Golden Coins.
"""
__author__ = "09x3086"

N = int(input())

a = int(N / 500)
b = int((N % 500) / 5)

x = a * 1000 + b * 5

print(x)
