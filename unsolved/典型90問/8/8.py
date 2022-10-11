# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
MOD = 10**9 + 7
# dpでしょ
# i(0-N)文字目まででk(0-7)文字完成させることができる選び方を記録するテーブルを作成
N = int(input())
S = input()[:-1]
dp = [[0] * 8 for i in range(N + 1)]
dp[0][0] = 1
atcoder_s = set(list("atcoder"))
counter = 0
for s in S:
    counter += 1
    dp[counter] = dp[counter - 1].copy()
    if s not in atcoder_s:
        continue
    if s == "a":
        dp[counter][1] += dp[counter - 1][0]
    if s == "t":
        dp[counter][2] += dp[counter - 1][1]
    if s == "c":
        dp[counter][3] += dp[counter - 1][2]
    if s == "o":
        dp[counter][4] += dp[counter - 1][3]
    if s == "d":
        dp[counter][5] += dp[counter - 1][4]
    if s == "e":
        dp[counter][6] += dp[counter - 1][5]
    if s == "r":
        dp[counter][7] += dp[counter - 1][6]
    for i in range(8):
        dp[counter][i] %= MOD
print(dp[N][7])
