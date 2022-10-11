# -*- coding: utf-8 -*-
# 8分
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
INF = 1 << 60
edges = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].add(b)
    edges[b].add(a)
find_next = deque([(0, 0)])
min_cost = [INF for i in range(n)]
while find_next:
    position, step = find_next.popleft()
    if min_cost[position] < step:
        continue
    min_cost[position] = step
    for next_position in edges[position]:
        find_next.append((next_position, step + 1))
for cost in min_cost:
    if cost == INF:
        print(-1)
        continue
    print(cost)
