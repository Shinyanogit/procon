# -*- coding: utf-8 -*-
#
import sys
from bisect import bisect_right

input = sys.stdin.readline
N = int(input())
# x間まで読めるかどうかの判定を行う関数で二分探索？
A = list(map(int, input().split()))
A.sort()
unneeded = 0


def readable(x):  # O(N)
    # 不要な漫画を全て売る
    less_than_x = bisect_right(A, x)
    over_x = N - less_than_x
    used = set()
    unneeded = 0
    for a in A[:less_than_x]:
        if a not in used:
            used.add(a)
        else:
            unneeded += 1
    # print(less_than_x)
    sold = unneeded + over_x
    return (len(used) + sold // 2) >= x


# for i in range(N):
# print(i, readable(i))

ok = 0
ng = N + 1
mid = (ok + ng) // 2
while ng - ok > 1:  # O(NlogN)
    if readable(mid):
        ok = mid
        mid = (ok + ng) // 2
    else:
        ng = mid
        mid = (ok + ng) // 2
print(ok)
