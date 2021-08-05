"""
A - Maxi-Buying.
"""
__author__ = "09x3086"

import math

N: float = int(input())

a: float = math.floor(N * 1.08)

answer: str = ""

if a < 206:
    answer = "Yay!"
if a == 206:
    answer = "so-so"
if a > 206:
    answer = ":("

print(answer)
