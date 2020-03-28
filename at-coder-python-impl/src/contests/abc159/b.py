# -*- coding:utf-8 -*-
"""
B - String Palindrome.
"""
__author__ = "09x3086"

N = input()

Answer = "No"
A = ""
B = ""
L = []

length = len(N)

if length % 2 == 1:
    for S in N:
        L.append(S)
    for k, v in enumerate(L):
        if k < (length - 1) / 2:
            A = A + v
    L = L[int(((length + 3) / 2) - 1):]
    for v in L:
        B = B + v

if A == B:
    Answer = "Yes"

print(Answer)
