# -*- coding: utf-8 -*-
#
import sys

MOD = 998244353
input = sys.stdin.readline
N, m = map(int, input().split())
ax, ay, bx, by, cx, cy = map(int, input().split())
blocks = set()
for i in range(m):
    a, b = map(int, input().split())
    blocks.add((a, b))


def noblock(i, j, k):
    x = ax * i + bx * j + cx * k
    y = ay * i + by * j + cy * k
    return (x, y) not in blocks


dp = [[[1]]]  # nij成分はn回のワープでa,bをij使った末たどり着ける場所への場合の和
for n in range(N):  # i回目での推移記録をもとにi+1回目の推移を記録
    resultn1 = [[[0 for k in range(n + 2)] for j in range(n + 2)] for i in range(n + 2)]
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            # print(n, i, j, k)
            start = dp[i][j][k]
            if noblock(i + 1, j, k):
                resultn1[i + 1][j][k] += start
            if noblock(i, j + 1, k):
                resultn1[i][j + 1][k] += start
            if noblock(i, j, k + 1):
                resultn1[i][j][k + 1] += start
    dp = resultn1.copy()
    # print(dp)
sumN = 0
for i in range(N + 1):
    for j in range(N - i + 1):
        sumN += dp[i][j][N - i - j]
print(sumN % MOD)
