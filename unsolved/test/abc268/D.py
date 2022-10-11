# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n = int(input())
# 深さ優先探索していくぜ
areas = set()
for i in range(n):
    x, y = map(int, input().split())
    areas.add((x, y))

# 探索済みの島は決していく
def dfs(x, y):  # (x,y)からcounter番目の島を探索
    global areas
    if (x, y) not in areas:
        return
    areas.remove((x, y))
    for dx, dy in [(1, 1), (1, 0), (0, 1)]:
        if (x + dx, y + dy) in areas:
            # print("dfs ", x + dx, y + dy)
            dfs(x + dx, y + dy)
        if (x - dx, y - dy) in areas:
            # print("dfs ", x - dx, y - dy)
            dfs(x - dx, y - dy)


counter = 0
for (x, y) in areas.copy():
    # print(areas)
    # print(x, y)
    if (x, y) not in areas:
        continue
    dfs(x, y)
    # print(areas, counter)
    counter += 1
print(counter)
