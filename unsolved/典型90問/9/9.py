# -*- coding: utf-8 -*-
# なんかTLEするんだよなぁ、、
import sys, math
from math import degrees as de
from math import atan2

input = sys.stdin.readline
N = int(input())
positions = []
for i in range(N):
    x, y = map(int, input().split())
    positions.append((x, y))
# 真ん中ともう一点を固定して3つ目の点に相応しいものを偏角に注目して二分探索する
def rotate(X, Y, sx, sy, d):
    # print(X, Y, sx, sy)
    x = X * sx + Y * sy
    y = -X * sy + Y * sx
    x /= d
    y /= d
    return (x, y)


def find_near180(degrees):
    left = 0
    right = len(degrees) - 1
    mid = (left + right) // 2
    while right - left > 2:
        if degrees[mid] > 180:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid
            mid = (left + right) // 2
    return 180 - min(180 - degrees[left], 180 - degrees[right])


def find_max_degree(
    center, side
):  # centerを中心に、sideを(1,0)に揃えるようにして座標を変換したのち、それ以外の点で180に最も近い偏角を返す
    cx, cy = positions[center]
    sx, sy = positions[side]
    d = (sx - cx) ** 2 + (sy - cy) ** 2
    d **= 0.5
    # print(sx, sy)
    degrees = []
    for i in range(N):
        if i == center or i == side:
            continue
        ax, ay = positions[i]
        # # print(ax, ay, sx, sy, cx, cy)
        # ax, ay = rotate(ax - cx, ay - cy, sx - cx, sy - cy, d)
        # if ay > 0 or (ay == 0 and ax > 0):
        #     if ay:
        #         rad = math.pi / 2 - math.atan(ax / ay)
        #     else:
        #         rad = 0
        # else:
        #     if ay:
        #         rad = math.pi / 2 + math.atan(ax / ay)
        #     else:
        #         rad = math.pi
        # degree = rad * 180 / math.pi
        degree = abs(de(atan2(ay - cy, ax - cx)))
        degrees.append(degree)
    degrees.sort()
    closest_degree = find_near180(degrees)
    return closest_degree


max_degree = 0
for center in range(N):
    for side in range(N):
        if side == center:
            continue
        max_degree = max(find_max_degree(center, side), max_degree)
        # print(center, side, max_degree)
print(max_degree)
