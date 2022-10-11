# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc106/tasks/abc106_d
import sys

input = sys.stdin.readline
n, m, q = map(int, input().split())
road = [[0] * n for i in range(n)]  # lr成分は区間[l,r]を直接結ぶ電車の数
for i in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    road[l][r] += 1
# 区間dpなきがする
dp = [[0] * n for i in range(n)]  # lr成分はlからrまでに含まれる路線の数
for i in range(n):
    dp[i][i] = road[i][i]
for r in range(1, n):
    for l in range(0, r):  # 区間[l,r]を考察
        dp[l][r] = dp[l][r - 1] + sum([road[i][r] for i in range(l, r + 1)])
for i in range(q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    print(dp[p][q])
