# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/dp/tasks/dp_x
import sys

input = sys.stdin.readline
N = int(input())
blocks = []
smax = 0
for i in range(N):
    w, s, v = map(int, input().split())
    blocks.append((s, w, v))
    if s > smax:
        w_of_smax = w
        smax = s
# 計算量から逆算するとO(N²logN程度が限界っぽい)
# dpしよう（i番目の軽さのブロックまでで、重さの限界wまでででの価値の最大値）
dp = [[0] * (smax + w_of_smax + 1) for i in range(N + 1)]
for i in range(1,N+1):
    for j in range(1,smax+w_of_smax+1):
        si,wi,wi=blocks[i-1]
        if j<=#i番目のブロックを下に敷ける
        dp[i][j]=
