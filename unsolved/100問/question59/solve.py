# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e
import sys
import heapq as hq

INF = 10**10

# ダイクストラ法を真剣にやる
n, k = map(int, input().split())
taxi = []  # タクシーの（料金、距離）
for i in range(n):
    cost, road = map(int, input().split())
    taxi.append((cost, road))
road = [[] for i in range(n)]  # 街iから行ける場所
for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)
min_cost = [INF for i in range(n)]  # 街iまでの最小費用
min_cost[0] = 0
search_hq = []  # 探索候補の（金、場所）を格納
hq.heapify(search_hq)


def make_candidate(k):  # 街kからタクシー乗って行ける新たな場所をsearch_hqにぶち込む
    cost, distance = taxi[k]
    tmp = [[(k, min_cost[k])]]  # ここに辿り着ける場所、料金をぶち込む
    for plus_step in range(1, distance + 1):
        tmp1 = []
        for city, start_cost in tmp[-1]:
            for next_city in road[city]:
                tmp1.append((next_city, min_cost[k] + cost))
        tmp.append(tmp1)
    # print(tmp)
    for line in tmp[1:]:
        for a, b in line:
            hq.heappush(search_hq, (b, a))
            # print("yen:", b, " city:", a)


make_candidate(0)
while search_hq:
    cost, start_city = hq.heappop(search_hq)
    # print(cost, min_cost[start_city], start_city)
    # if start_city == n - 1:
    #     print(cost)
    #     print(min_cost)
    #     exit()
    if min_cost[start_city] > cost:  # 未踏か、更新の余地あり
        min_cost[start_city] = cost
        # print(min_cost)
        # print(start_city, cost)
        make_candidate(start_city)
print(min_cost[-1])
