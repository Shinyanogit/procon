# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/arc035/tasks/arc035_c
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# road_list = [[] for i in range(n)]  # (目的地、距離)
cost = [[float("inf")] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    cost[a][b] = c
    cost[b][a] = c
for i in range(n):
    cost[i][i] = 0
for k in range(n):  # 0-k都市を経由
    for i in range(n):
        for j in range(n):  # iからjまでの道のりを計算
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
calc_S = lambda some_list: sum([sum(some_list[i]) for i in range(n)]) // 2
k = int(input())
for i in range(k):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    for start in range(n):
        for goal in range(n):
            cost[start][goal] = min(
                cost[start][goal],
                cost[start][x] + z + cost[y][goal],
                cost[start][y] + z + cost[x][goal],
            )
    print(calc_S(cost))
