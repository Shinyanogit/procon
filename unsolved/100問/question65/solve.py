# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joisc2010/tasks/joisc2010_finals
# メモリ制限でpythonでしか通らなかった
import sys
import heapq as hq
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


# 各国が代表を派遣
input = sys.stdin.readline
n, m, k = map(int, input().split())
rail_hq = []
hq.heapify(rail_hq)
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    hq.heappush(rail_hq, (c, a, b))
# あとは短い順に結んでいき、その際新たに道路を開通させるたびにコストを記録していく
uf = UnionFind(n)
cost_list = [0]
cost = 0
counter = 0  # 今まで開通させた道路の本数
while counter < n - k:
    c, a, b = hq.heappop(rail_hq)
    if uf.same(a, b):  # 繋がっている
        continue
    uf.union(a, b)
    cost += c
    counter += 1
    # cost_list.append(cost)
# 最後のk-1辺を取り除いて開通コストを計算する
# print(cost_list[max(n - k, 1)])
print(cost)
