# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
import sys

input = sys.stdin.readline
MOD = 10**4
N, K = map(int, input().split())
A = [0] * N  # i成分はi+1日目に食べないといけないパスタ(ただし0は未指定)
for k in range(K):
    a, b = map(int, input().split())
    A[a - 1] = b
dp = [
    [[0] * 4 for i in range(4)] for j in range(N + 1)
]  # iをn日前に食べjをn-1日前に食べているような、n(0-N)日目までのパターン数をdp[n][i][j]として表します。
dp[0][0][0] = 1
for n in range(N):
    for i in range(4):
        for j in range(4):  # n日目にi,n-1日目にjを食べた通りを使ってn+1日目にkを食べる通りを表す
            for k in range(1, 4):
                if A[n] != 0 and A[n] != k:
                    continue
                if i != j or j != k:  # ３日連速ではない場合
                    dp[n + 1][k][i] += dp[n][i][j]
                    dp[n + 1][k][i] %= MOD
ans = 0  # 最終日、全ての通りを足す
for i in range(1, 4):
    for j in range(1, 4):
        ans += dp[N][i][j]
        ans %= MOD
print(ans)
