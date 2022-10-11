# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc012/tasks/abc012_4
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
road_list = [
    [float("inf")] * n for i in range(n)
]  # i成分はi番目のバス停から到着できる場所と、そこまでの距離のsetリスト
for i in range(m):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    road_list[a][b] = t
    road_list[b][a] = t
# ここからスタート地点を全て試して最悪の経路を列挙していく
def warshall():  # 地点iから地点jまでの最短距離をワーシャルフロイド法で求めリストで出力する
    cost = road_list  # 各地点の最短到達時刻を打刻
    for k in range(n):  # 0-k駅を使う
        cost[k][k] = 0
        for i in range(n):  # i駅から
            for j in range(n):  # j駅まで
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost


ans = float("inf")
dp = warshall()
for distance_list in dp:
    ans = min(ans, max(distance_list))
# print(dp)
print(ans)
