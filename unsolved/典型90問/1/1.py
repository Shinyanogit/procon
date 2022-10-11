# -*- coding: utf-8 -*-
#
import sys
import heapq as hq

input = sys.stdin.readline
n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
pieces = [a[0]]
for i in range(len(a) - 1):
    pieces.append(a[i + 1] - a[i])
pieces.append(l - a[-1])
# サイズの最低値を指定してK+1ピース以上に分散させることが実現可能か判定する関数を作って、二分探索
def min_size_ok(size):  # O(n)
    length = 0
    counter = 0
    # print("size:", size)
    for piece in pieces:
        length += piece
        if length >= size:
            # print(length)
            length = 0
            counter += 1
    return counter >= k + 1


def find_min_limit_max():  # 0(logl)
    ok = 0
    ng = l
    mid = (ok + ng) // 2
    while ng - ok > 1:
        # print("------")
        if min_size_ok(mid):
            ok = mid
            mid = (ok + ng) // 2
        else:
            ng = mid
            mid = (ng + ok) // 2
    return mid


print(find_min_limit_max())
