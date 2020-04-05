# -*- coding:utf-8 -*-
"""
F - Knapsack for All Segments.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

dp = [[[0 for i in range(N[1] + 1)] for j in range(N[0] + 1)] for k in range(3)]
dp[0][0][0] = 1

p = 998244353

for i in range(N[0]):
    for j in range(N[1] + 1):
        dp[0][i + 1][j] = (dp[0][i + 1][j] + dp[0][i][j]) % p
        dp[1][i + 1][j] = (dp[1][i + 1][j] + dp[0][i][j] + dp[1][i][j]) % p
        dp[2][i + 1][j] = (dp[2][i + 1][j] + dp[0][i][j] + dp[1][i][j] +
                           dp[2][i][j]) % p
        if j + M[i] <= N[1]:
            dp[1][i + 1][j + M[i]] = (dp[1][i + 1][j + M[i]] + dp[0][i][j] +
                                      dp[1][i][j]) % p
            dp[2][i + 1][j + M[i]] = (dp[2][i + 1][j + M[i]] + dp[0][i][j] +
                                      dp[1][i][j]) % p

print(dp[2][N[0]][N[1]])
