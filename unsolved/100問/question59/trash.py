# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e
import sys
import heapq as hq

input = sys.stdin.readline
n, k = map(int, input().split())
# 多分これダイクストラ法っすね
taxi = []  # i成分は街iでのタクシー事情
INF = 10**10
for i in range(n):
    cost, road = map(int, input().split())
    taxi.append((cost, road))
road = [[] for i in range(n)]  # i成分は街iから到達できる街のリスト
for j in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)
min_cost = [INF for i in range(n)]  # i成分は街iまでの最安値を保存
min_cost[0] = 0
search_hq = []  # 捜索する候補地点について、コストと場所を格納
hq.heapify(search_hq)


def search(
    k, start_cost,num,taxi_cost
):  # start_costの確定している街kからcostのタクシーをnum回使える状態から到達できる範囲をhqにぶち込んでいく
    if num:  # まだ進める
        # cost0 = start_cost
        cost, road = taxi[k]
        next_cities = road[k]
        for city in next_cities:
            if min_cost[city] == INF:  # まだ未踏
                hq.heappush((cost + start_cost, city))  # 到達地点の追加
                search(city, start_cost + cost, num - 1)


search(0)
while search_hq:
    cost, city = hq.heappop(search_hq)  # 次の指針
    min_cost[city] = cost
    search(city,cost,taxi[])
