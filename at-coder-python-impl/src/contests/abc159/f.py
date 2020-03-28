# -*- coding:utf-8 -*-
"""
F - Knapsack for All Segments.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

dp = [[[0 for i in range(N[0] + 1)] for j in range(N[1] + 1)] for k in range(3)]
dp[0][0][0] = 1

p = 998244353

for i in range(N[0] - 1):
    for j in range(N[1] - 1):
        dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][0]) % p
        dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][1]) % p
        dp[i + 1][j][2] = (dp[i + 1][j][2] + dp[i][j][2]) % p
        if j + M[i] <= N[1]:
            dp[i + 1][j + M[i]][1] = (dp[i + 1][j + M[i]][1] + dp[i][j][0] +
                                      dp[i][j][1]) % p
            dp[i + 1][j + M[i]][2] = (dp[i + 1][j + M[i]][1] + dp[i][j][0] +
                                      dp[i][j][1]) % p

print(dp)
