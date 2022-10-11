# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc134/tasks/abc134_e
import sys

input = sys.stdin.readline
# これこそ典型的なdp
n = int(input())
a = [int(input()) for i in range(n)]
dp = [[a[0]], [a[0]]]  # i成分はA0-Aiまででの最小種類での色分けと、各色の最大値のリスト(小さい順にソート済み)
for i in range(1, n):  # AiをAi-1をもとに考える
    flag = True
    colour_num = len(dp[-1])
    for j in range(colour_num):
        # print(i, j, dp)
        if dp[i - 1][-j - 1] < a[i]:
            dp[i][-j - 1] = a[i]
            dp.append(dp[-1])
            dp[i].sort()
            flag = False
            break
    if flag:
        dp.append(dp[-1])
        dp[i].append(a[i])
        dp.sort()
# print(dp[-1])
print(len(dp[-1]))
