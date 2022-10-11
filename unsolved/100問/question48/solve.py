# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 因縁の相手、ここで潰す
# 区間dpっぽい
# TLEらしい、○ね
while True:
    n = int(input())
    if n == 0:
        exit()
    w_list = list(map(int, input().split()))
    dp = [[-1] * n for i in range(n)]  # ij成分は区間[i,j]で落とせる総数
    for i in range(n):
        dp[i][i] = 0

    def clash(i, j):  # 区間[i,j]で落とせる総数
        if j - i < 2:
            return 0
        if dp[i][j] >= 0:
            return dp[i][j]
        elif -2 < w_list[i] - w_list[j] < 2 and clash(i + 1, j - 1) == j - i - 1:
            dp[i][j] = j - i + 1
            return j - i + 1
        else:  # 間を落としていく
            max_daruma = 0
            for k in range(i + 1, j):
                max_daruma = max(clash(i, k) + clash(k + 1, j), max_daruma)
            dp[i][j] = max_daruma
            return max_daruma

    print(clash(0, n - 1))
