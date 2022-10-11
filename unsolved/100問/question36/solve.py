# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
# なんかREになる
import sys

input = sys.stdin.readline
n, w = map(int, input().split())
v_list = []
w_list = []
for i in range(n):
    a, b = map(int, input().split())
    v_list.append(a)
    w_list.append(b)
# 部分問題を種類だけにすると漸化式が作れない
# 重さも情報に含めてはどうか？
dp = [[0] * (w + 1) for i in range(n)]  # ij成分はi番目までで重さ制限jの時の最大値
# まず0番目までで考える
w0 = w_list[0]
v0 = v_list[0]
if w0 <= w:
    for j in range(0, w + 1):
        dp[0][j] = (j // w0) * v0
for i in range(1, n):  # i(0-n-1)番目までで
    for j in range(1, w + 1):  # 重さjまでの価値の最大化
        v1 = v_list[i]
        w1 = w_list[i]
        if j >= w1:
            candidate = [dp[i - 1][j - c * w1] + c * v1 for c in range(j // w1 + 1)]
            dp[i][j] = max(candidate)
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])
# for line in dp:
#     print(line)
