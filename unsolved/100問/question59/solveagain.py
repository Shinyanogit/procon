# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e
import sys

input = sys.stdin.readline
# 多分ダイクストラ法
n, k = map(int, input().split())
import heapq as hq

neighbor_hq = [(0, 0)]  # 探索対象の(コスト、場所)
hq.heapify(neighbor_hq)
taxi = []
for i in range(n):
    c, r = map(int, input().split())
    taxi.append((c, r))
rail = [[] for i in range(n)]  # 街iから行ける街のリスト
for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    rail[a].append(b)
    rail[b].append(a)
min_cost = [float("INF") for i in range(n)]  # 街iにいくのにかかるコスト
min_cost[0] = 0


def get_neighbor(
    station, step_left, fee, start_cost
):  # ある街からstep_left以内にfee円で探索できる未踏の地点を(コスト、場所)のリストで返す
    global neighbor_hq
    bucket = []
    if step_left == 0:
        return
    for neighbor in rail[station]:
        get_neighbor(neighbor, step_left - 1, fee, start_cost)
        if min_cost[neighbor] > start_cost + fee:
            hq.heappush(neighbor_hq, (start_cost + fee, neighbor))


cost0, step0 = taxi[0]
get_neighbor(0, step0, cost0, 0)
while neighbor_hq:
    cost, station = hq.heappop(neighbor_hq)
    # print(cost, station)
    if min_cost[station] > cost:
        min_cost[station] = cost
        fee, step_left = taxi[station]
        get_neighbor(station, step_left, fee, cost)
print(min_cost[-1])
