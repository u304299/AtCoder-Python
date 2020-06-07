# -*- coding:utf-8 -*-
"""
A - ABC Swap.
"""
__author__ = "09x3086"

x, y, z = map(int, input().split())

answerList = [z, x, y]

for i in range(len(answerList)):
    print(answerList[i], end=' ')
