# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# メモリ制限らしい、クソワロタ
import sys
from bisect import bisect_right

input = sys.stdin.readline
n, m = map(int, input().split())
point = [int(input()) for i in range(n)]
point.append(0)
point.sort()
# 2本だけ使って取れる点数のリスト（O(n²)）
point2 = []
for p1 in point:
    for p2 in point:
        point2.append(p1 + p2)
point2 = list(set(point2))
# こっから各点数に対してあと何点取れるかを考えて、それ以下のpoint2内で最大の点数を足していく。(O(n²logn))
ans = 0
for point in point2:
    margin = m - point
    y = bisect_right(point2, margin)
    if y > 0:
        ans = max(ans, point + point2[y - 1])
    if ans == m:
        break
print(ans)
