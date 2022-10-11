# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/tkppc4-1/tasks/tkppc4_1_h
import sys, heapq

# なんかバグる
input = sys.stdin.readline
n, m, k = map(int, input().split())
transfer = [0] + [int(input()) for i in range(n - 2)] + [0]  # i成分は駅iでの乗り換え所要時間
paths = [[] for i in range(n)]  # i成分は駅iから伸びる路線情報（到着駅、所要時間、運行状況）
for i in range(m):
    a, b, c, d = map(int, input().split())
    a, b = a - 1, b - 1
    paths[a].append((b, c, d))
    paths[b].append((a, c, d))
cost = [float("inf") for i in range(n)]  # 駅iまでの最短到達時間
search_hq = [(0, 0)]  # 時間:駅
cost[0] = 0
while search_hq:
    time, station = heapq.heappop(search_hq)
    if time > cost[station]:
        continue
    for next_station, t, span in paths[station]:
        transfered = time + transfer[station]
        departure = transfered % span + transfered
        arrival = departure + t
        # print(next_station, time, transfered, departure, arrival)
        if arrival < cost[next_station]:
            cost[next_station] = arrival
            heapq.heappush(search_hq, (arrival, next_station))
if cost[-1] <= k:
    print(cost[n - 1])
else:
    print(-1)
# print(cost)
