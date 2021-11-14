"""
C - Swappable.
"""
__author__ = "09x3086"
# TODO

N = int(input())
M = [int(x) for x in input().split()]

money: int = 0
answer: int = 0

while N > money:
    answer += 1
    money += answer

print(answer)
