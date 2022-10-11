# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2017yo/tasks/joi2017yo_d
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
csum = [[0] * (N + 1) for _ in range(M)]
for i in range(N):
    k = int(input())
    k -= 1
    csum[k][i + 1] = 1
for k in range(M):
    for i in range(1, N + 1):
        csum[k][i] += csum[k][i - 1]
num = [csum[k][-1] for k in range(M)]

dp = [float("inf")] * (1 << M)
dp[0] = 0
for S in range(1 << M):
    tot = 0
    for x in range(M):
        if S & 1 << x:
            tot += num[x]
    for x in range(M):
        if not S & 1 << x:
            dp[S ^ 1 << x] = min(
                dp[S ^ 1 << x], dp[S] + num[x] - csum[x][tot + num[x]] + csum[x][tot]
            )
print(dp[-1])
