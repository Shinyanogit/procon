# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
# RE！！！！
import sys

input = sys.stdin.readline


class Group:
    def __init__(self, w, h, position):
        # self.groups = [(0, 0)]
        self.walkable = position
        self.walked = [[False] * w for i in range(h)]
        self.island_num = 0

    def search(self, i, j):
        if not self.walked[i][j]:
            self.walked[i][j] = True
            # self.groups[-1].append((i,j))
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    if 0 <= x < h and 0 <= y < w and self.walkable[i][j]:
                        self.search(x, y)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    position = [list(map(int, input().split())) for i in range(h)]
    groupclass = Group(w, h, position)
    for i in range(h):
        for j in range(w):
            if groupclass.walkable[i][j] and not groupclass.walked[i][j]:
                groupclass.island_num += 1
                groupclass.search(i, j)
    print(groupclass.island_num)
