# -*- coding: utf-8 -*-
# グラフが一つ余分なので、ループが一つできる
# ループの中にあるに頂点はパスがふた通りできてしまうし、そうでなければ単純パスと言えるはず
# そのため、一位に定まるか定まらないかはまずループの辺を全て切断して、その後根っこが一緒かどうか
import sys

input = sys.stdin.readline
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


N = int(input())
edges = [[] for i in range(N)]
edges_set = set()
for i in range(N):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
    edges_set.add((u, v))
# ループをdfsで見つける
end_flag = False


def dfs(log_set, log, next_position):
    print(76, log, next_position)
    answer = []
    global end_flag
    if len(log) >= 2:
        if log[-2] == next_position:
            print(81, log, next_position)
            return []
    if end_flag:
        return []
    if next_position in log_set:
        print(85, log, next_position)
        loop = log[log.index(next_position) :]
        end_flag = True
        answer = loop
        return answer
    log.append(next_position)
    log_set.add(next_position)
    print(92, edges[next_position])
    for the_next in edges[next_position]:
        print(94, edges[next_position])
        answer = dfs(log_set, log, the_next)
        if len(answer):
            return answer
    log = log[:-1]
    return []  # 行き止まり


for n in edges[0]:
    loop = dfs(set([0]), [0], n)
    if len(loop):
        break
print(loop)
loop = set(loop)
tree = UnionFind(N)
for u, v in edges_set:
    if u in loop and v in loop:
        continue
    tree.union(u, v)
Q = int(input())
for q in range(Q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if tree.same(x, y):
        print("Yes")
    else:
        print("No")
