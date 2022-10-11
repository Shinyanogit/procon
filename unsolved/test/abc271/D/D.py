# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, S = map(int, input().split())
# 絶対dp
# i枚目までを使ってjという値が表現できるかを判定するテーブルを考える
dp = [[0] * (S + 1) for i in range(N + 1)]
card_order = [[""] * (S + 1) for i in range(N + 1)]
dp[0][0] = 1


def show():
    for line in dp:
        print(dp)


for i in range(N):
    a, b = map(int, input().split())
    for j in range(S + 1):
        if j >= a and dp[i][j - a]:
            dp[i + 1][j] = 1
            card_order[i + 1][j] = card_order[i][j - a] + "H"
        if j >= b and dp[i][j - b]:
            dp[i + 1][j] = 1
            card_order[i + 1][j] = card_order[i][j - b] + "T"
    # print(dp[i + 1])
if dp[N][S]:
    print("Yes")
    print(card_order[N][S])
else:
    print("No")
    print(card_order[N][S])
