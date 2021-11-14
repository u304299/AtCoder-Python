"""
B - Savings.
"""
__author__ = "09x3086"

N: float = int(input())

money: int = 0
answer: int = 0

while N > money:
    answer += 1
    money += answer

print(answer)
