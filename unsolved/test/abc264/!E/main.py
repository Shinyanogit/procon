# -*- coding: utf-8 -*-
# 仮想電源を中心に放射状に電源を繋いでいく。仮想電源と同じ島であるかが電気が通っているかとイコール
import sys
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


input = sys.stdin.readline
N, M, E = map(int, input().split())
# 全て切ってから繋いでいくのがとても健康的
edges = []
tree = UnionFind(N + M + 1)
for i in range(N, N + M):  # まず仮想電源を中心に電源を繋ぐ
    tree.union(i, N + M)
for i in range(E):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges.append((u, v))
Q = int(input())
X = [int(input()) for i in range(Q)]
X_set = set(X)
for i, e in enumerate(edges):  # その後、Q本のエッジを除いて繋いでいく
    if i + 1 in X_set:
        continue
    u, v = e
    print(u, v)
    tree.union(u, v)
# 最後に、一本づつ繋いでいく
answer = [0 for i in range(Q)]
answer[-1] = tree.size(N + M) - 1 - M
print(tree.members(N + M))
index = Q - 1
for i in range(Q - 1, 0, -1):
    u, v = edges[X[i] - 1]
    if tree.same(u, v):
        answer[index - 1] = answer[index]
        index -= 1
        print(tree.members(N + M))
        continue
    else:
        tree.union(u, v)
        answer[index - 1] = tree.size(N + M) - 1 - M
        index -= 1
        print(tree.members(N + M))
        continue
for a in answer:
    print(a)
