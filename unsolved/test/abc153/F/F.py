# -*- coding: utf-8 -*-
# 左から貪欲に当てよう
import sys
import heapq as hq

input = sys.stdin.readline
N, D, A = map(int, input().split())
monsters_hq = [tuple(map(int, input().split())) for i in range(N)]
hq.heapify(monsters_hq)
counter = 0
while monsters_hq:
    # print(monsters_hq, 12)
    x, h = hq.heappop(monsters_hq)
    count = (h - 1) // A + 1
    # print("count", count)
    bucket = []
    while monsters_hq:
        # print(monsters_hq, 16)
        x1, h1 = hq.heappop(monsters_hq)
        if x1 > x + 2 * D:
            bucket.append((x1, h1))
            break
        if h1 > D * count:
            bucket.append((x1, h1 - D * count))
            # hq.heappush(monsters_hq, (x1, h1 - D * count))
    for x2, h2 in bucket:
        hq.heappush(monsters_hq, (x2, h2))
    counter += count
print(counter)
