# -*- coding: utf-8 -*-
# 貪欲方ではなさそう
# hについてのdpっぽい
# 更新にO(N)だから結構きつい
INF = 1 << 60
import sys

input = sys.stdin.readline
H, N = map(int, input().split())
magics = [tuple(map(int, input().split())) for i in range(N)]
magics.sort(reverse=True)
# print(magics)
min_mp = [0 for h in range(H + 1)]  # h成分は体力hの敵を倒すのに必要な魔力の最小値


def Min_mp(h):
    if h <= 0:
        return 0
    else:
        return min_mp[h]


for h in range(1, H + 1):
    min_cost = INF
    for damage, mp in magics:
        # if h > damage:
        # break
        min_cost = min(Min_mp(h - damage) + mp, min_cost)
    min_mp[h] = min_cost
print(min_mp[H])
