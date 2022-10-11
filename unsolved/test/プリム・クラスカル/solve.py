# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f
# まずプリム法で実装してみる
import sys, heapq

input = sys.stdin.readline
n, m = map(int, input().split())
paths = [[] for i in range(n)]  # i成分はiつ目の街から伸びている道路の情報(距離、行き先)
for i in range(m):
    u, v, c = map(int, input().split())
    paths[u].append((c, v))
    paths[v].append((c, u))
search_hq = paths[0]  # 探索する距離、行き先
heapq.heapify(search_hq)
total_cost = 0
marked = [False for i in range(n)]
marked[0] = True
while search_hq:
    c, city = heapq.heappop(search_hq)
    if marked[city]:
        continue
    total_cost += c
    marked[city] = True
    # 探索先を追加
    for cost, next_city in paths[city]:
        heapq.heappush(search_hq, (cost, next_city))
print(total_cost)
