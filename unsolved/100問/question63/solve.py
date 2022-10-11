# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc074/tasks/arc083_b
import sys

input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    cost[i][i] = float("inf")
# u-w-vというような経路で最短距離を求めて、直接結ぶ必要があるかを検討
ans = 0
for u in range(N):
    for v in range(u + 1, N):
        mn = float("inf")
        for w in range(N):
            mn = min(mn, cost[u][w] + cost[w][v])
        if cost[u][v] > mn:  # ありえない
            print(-1)
            exit()
        elif cost[u][v] < mn:  # 直接結ぶのが最短
            ans += cost[u][v]
print(ans)
