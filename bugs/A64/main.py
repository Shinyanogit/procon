# -*- coding: utf-8 -*-
# 重み付きグラフの全探索→ダイクストラだね
import sys
import heapq as hq

input = sys.stdin.readline
N, M = map(int, input().split())
INF = 1 << 60
edges = [set() for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].add((c, b))
    edges[b].add((c, a))
min_cost = [INF for i in range(N)]
# print(edges)
reached_positions = 0
search_hq = [(0, 0)]
hq.heapify(search_hq)


def dikstra(cost, i):  # 頂点iにcostをかけて進み、探索範囲を更新する
    global reached_positions
    if min_cost[i] < cost:
        return
    min_cost[i] = cost
    reached_positions += 1
    for plus_cost, next_node in edges[i]:
        hq.heappush(search_hq, (cost + plus_cost, next_node))


while search_hq:
    if reached_positions == N:
        for e in min_cost:
            print(e)
        exit()
    # print(search_hq)
    cost, i = hq.heappop(search_hq)
    dikstra(cost, i)
