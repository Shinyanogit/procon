# -*- coding: utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127
import sys
from math import sqrt as r


input = sys.stdin.readline
# クラスカル法かなぁ、短い順に辺を選んで小さい枝からくっつけてこ
from collections import defaultdict


class UnionFind:  # おまじない
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


def distance(position1, position2):
    x1, y1, z1, r1 = position1
    x2, y2, z2, r2 = position2
    return max(r((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) - (r2 + r1), 0)


while True:
    n = int(input())
    if n == 0:
        break
    edges = []  # i成分は(距離、スタート、ゴール)
    uf = UnionFind(n)
    position = []
    for i in range(n):
        # まずcellを読み込んでからグラフを作ろう！
        position.append(list(map(float, input().split())))
    # 次に距離を計算してグラフを作ろう！
    for i in range(n - 1):  # スタート
        for j in range(i + 1, n):  # ゴール
            distanceij = distance(position[i], position[j])
            if distanceij:  # 繋がっていない
                edges.append((distanceij, i, j))
            else:  # 繋がっている
                uf.union(i, j)
    edges.sort()
    # さあこれから短いものを順に選んでいくぞう
    total_length = 0
    for edge in edges:
        d, u, v = edge
        if uf.same(u, v):
            continue
        total_length += d
        uf.union(u, v)
    answer = str(round(total_length, 3))
    a = answer.split(".")
    # print(answer)
    # print(a)
    a1 = a[0]
    if len(a) == 1:
        a2 = "000"
    elif float(a[1]) * 100 - 100 * int(a[1]) == 0:  # 100倍すると整数に
        a2 = a[1]
        while True:
            if len(a2) == 3:
                break
            a2 += "0"
    answer = a1 + "." + a2
    print(answer)
    # print(a1, a2)
    # print()
