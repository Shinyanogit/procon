# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
import sys

input = sys.stdin.readline
# 各々の注文に対して全ての店舗を検討するのはO(nm)で無理
# まず店舗を時計回りにソートして(O(nlogn))その後各注文に二分探索で最適な店舗を割り当てる(O(mlogn))
[d, n, m] = [int(input()) for i in range(3)]
shop = [0] + [int(input()) for i in range(n - 1)]
for d_shop in shop.copy():
    shop.append(d_shop + d)
    shop.append(d_shop - d)
shop.sort()
total_distance = 0
for i in range(m):
    destination = int(input())  # 目的地に最も近いshopを炙り出す
    left = 0
    right = 3 * n - 1
    mid = (left + right) // 2
    while right - left > 1:
        if shop[mid] < destination:
            left = mid
            mid = (left + right) // 2
        else:
            right = mid
            mid = (left + right) // 2
    total_distance += min(shop[right] - destination, destination - shop[left])
print(total_distance)
