# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
import sys

# pythonだとどうしてもTLEになってしまう


def find_max_subsequence_size(x, y):
    size_x = len(x)
    size_y = len(y)
    dp = [
        [0 for i in range(len(y) + 1)] for i in range(len(x) + 1)
    ]  # ij成分はx[:i]とy[:j]の最長共通部分列の長さ
    for i in range(1, size_x + 1):
        for j in range(1, size_y + 1):
            d = 0
            if x[i - 1] == y[j - 1]:
                d = 1
            dp[i][j] = max(dp[i - 1][j - 1] + d, dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


input = sys.stdin.readline
q = int(input())
for i in range(q):
    x = input().split("\n")[0]
    y = input().split("\n")[0]
    print(find_max_subsequence_size(x, y))
