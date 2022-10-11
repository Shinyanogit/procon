# -*- coding: utf-8 -*-
#
import sys

INF = 1 << 60
input = sys.stdin.readline
N, M, K = map(int, input().split())
# Eの部分列のk文字目までを使用していける場所の最短距離を更新していく
min_cost = [INF for i in range(N)]
paths = []
for i in range(M):
    a, b, c = map(int, input().split())
    paths.append((a - 1, b - 1, c))
min_cost[0] = 0
E = list(map(int, input().split()))
for e in E:
    city1, city2, cost = paths[e - 1]
    if min_cost[city1] < INF:  # city1まで到達可能
        min_cost[city2] = min(min_cost[city2], min_cost[city1] + cost)
    # if min_cost[city2] < INF:
    # min_cost[city1] = min(min_cost[city1], min_cost[city2] + cost)
if min_cost[N - 1] < INF:
    print(min_cost[-1])
else:
    print(-1)
