# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc007/tasks/abc007_3
import sys
import heapq as hq

INF = 10**9

input = sys.stdin.readline
R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1
maze = [list(input()) for i in range(R)]
neighbor_hq = []  # 近隣の探索によって辿り着ける未踏の地の(歩数、座標)
hq.heapify(neighbor_hq)
min_distance = [[INF] * C for i in range(R)]
min_distance[sx][sy] = 0


def around(x, y):  # (x,y)周辺で未踏かつ進める座標を列挙
    bucket = []
    for X, Y in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
        if maze[X][Y] == "." and min_distance[X][Y] == INF:
            bucket.append((X, Y))
    # print("around ", (x, y), ":", bucket)
    return bucket


def get_neighbor(x, y, step):  # 歩数stepにして(x,y)からスタートしてneighbor_hqに近隣を追加
    global neighbor_hq
    for X, Y in around(x, y):
        # if (X, Y) == (3, 2):
        # print("from ", (x, y, step), " to ", (3, 2))
        # if (x, y) == (1, 1):
        # print("around (1,1)", X, Y)
        hq.heappush(neighbor_hq, (step + 1, (X, Y)))


get_neighbor(sx, sy, 0)
while neighbor_hq:
    step, (x, y) = hq.heappop(neighbor_hq)
    if min_distance[x][y] > step:
        # print(x, y, step)
        min_distance[x][y] = step
        get_neighbor(x, y, step)
print(min_distance[gx][gy])
