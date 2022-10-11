# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc074/tasks/arc083_b
import sys

input = sys.stdin.readline
# クラスカル法を使ってみよう
# あとがき、最小木をつくってcost計算だけなら十分、妥当性チェックはできなそう
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


n = int(input())
uf = UnionFind(n)
edges = []
for i in range(n):
    alist = list(map(int, input().split()))
    for j in range(n):
        c = alist[j]
        edges.append((c, i, j))
edges.sort()
cost = 0
distance = [[float("inf")] * n for i in range(n)]
for i in range(n):
    distance[i][i] = 0
for edge in edges:
    c, u, v = edge
    print(edge)
    if not uf.same(u, v):  # 繋がってない
        uf.union(u, v)
        distance[u][v] = c
        distance[v][u] = c
        # uへの到着ルート、vへの到着ルートを更新する
        for i in range(n):
            distance[i][u] = min(distance[i][u], distance[i][v] + c)
            distance[i][v] = min(distance[i][v], distance[i][u] + c)
            distance[v][i] = distance[i][v]
            distance[u][i] = distance[i][u]
        cost += c
    # else:  # 繋がっているなら妥当性チェック
    #     if distance[u][v] != c:
    #         print(u, v)
    #         print(distance)
    #         print(-1)
    #         sys.exit()
print(distance)
print(cost)
