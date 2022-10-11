# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp
import sys
import heapq as hq

input = sys.stdin.readline
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    movable_places = [[[] for i in range(w)] for j in range(h)]
    for height in range(h):
        walls_right = list(map(int, input().split()))
        # print(walls_right)
        for width in range(w - 1):
            if not walls_right[width]:
                movable_places[height][width].append((height, width + 1))
                movable_places[height][width + 1].append((height, width))
        if height == h - 1:
            break
        walls_down = list(map(int, input().split()))
        # print(walls_down)
        for width in range(w):
            if not walls_down[width]:
                movable_places[height][width].append((height + 1, width))
                movable_places[height + 1][width].append((height, width))
    search_hq = []  # 距離、x,y
    for x, y in movable_places[0][0]:
        search_hq.append((1, x, y))
    hq.heapify(search_hq)
    min_distance = [[float("inf") for i in range(w)] for i in range(h)]
    min_distance[0][0] = 0
    while search_hq:
        d, x, y = hq.heappop(search_hq)
        if min_distance[x][y] > d:
            min_distance[x][y] = d
            for neighbor in movable_places[x][y]:
                x, y = neighbor
                hq.heappush(search_hq, (d + 1, x, y))
    distance = min_distance[-1][-1] + 1
    if distance < w * h:
        print(distance)
    else:
        print(0)
