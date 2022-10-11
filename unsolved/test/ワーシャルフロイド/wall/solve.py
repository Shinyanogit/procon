# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc079/tasks/abc079_d
import sys

input = sys.stdin.readline
h, w = map(int, input().split())
cost = [list(map(int, input().split())) for i in range(10)]
minimum_cost = cost  # ここから書き換えていく
for k in range(10):  # 0-kをつかう
    for i in range(10):
        for j in range(10):  # iからjまで変化させる
            minimum_cost[i][j] = min(
                minimum_cost[i][j], minimum_cost[i][k] + minimum_cost[k][j]
            )
minimum_cost = [minimum_cost[i][1] for i in range(10)]
sum = 0
for i in range(h):
    blocks = list(map(int, input().split()))
    for block in blocks:
        if block + 1:
            sum += minimum_cost[block]
print(sum)
