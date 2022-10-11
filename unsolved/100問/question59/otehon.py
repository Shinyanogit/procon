# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
import heapq

INF = 10**10


def dijkstra(s, g):
    dists = [INF for i in range(N)]
    dists[s] = 0
    pq = [(0, s)]  # 優先度付きキューのオブジェクトそのものはただのリスト
    while pq:
        d, node = heapq.heappop(pq)
        if d > dists[node]:  # 探索の対象にする必要があるか確認
            continue
        for next, cost in adj[node]:
            if d + cost < dists[next]:
                dists[next] = d + cost
                heapq.heappush(pq, (dists[next], next))
    if dists[g] == INF:
        return -1
    else:
        return dists[g]


N, K = map(int, input().split())
adj = [[] for i in range(N)]
ans = []
for k in range(K):
    ls = list(map(int, input().split()))
    if ls[0] == 0:
        ans.append(dijkstra(ls[1] - 1, ls[2] - 1))
    else:
        adj[ls[1] - 1].append((ls[2] - 1, ls[3]))
        adj[ls[2] - 1].append((ls[1] - 1, ls[3]))
for a in ans:
    print(a)
