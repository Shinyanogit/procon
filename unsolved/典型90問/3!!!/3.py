# -*- coding: utf-8 -*-
#
import sys

sys.setrecursionlimit(10**8)

INF = 1 << 60

input = sys.stdin.readline
n = int(input())
paths = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    paths[a].append(b)
    paths[b].append(a)
min_distance = [INF for i in range(n)]
min_distance[0] = 0
max_index = 0
max_distance = 0


def dfs(start, d):  # スタート地点から一つ進んで、最短距離を更新する
    global min_distance, max_index, max_distance
    for neighbor in paths[start]:
        if min_distance[neighbor] > d + 1:
            min_distance[neighbor] = d + 1
            if d + 1 > max_distance:
                max_distance = d + 1
                max_index = neighbor
            dfs(neighbor, d + 1)


dfs(0, 0)
end_node = max_index
min_distance = [INF for i in range(n)]
min_distance[end_node] = 0
max_distance = 0
dfs(end_node, 0)
print(max_distance + 1)
