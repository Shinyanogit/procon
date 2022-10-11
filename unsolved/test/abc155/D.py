# -*- coding: utf-8 -*-
# 18分経過
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
# 少しづつ使えるaを解放していって、k番目までの数字を解放していく
a = list(map(int, input().split()))
a.sort()
# 小さいaから解放していく
# 最新のaが正なら小さい数から、負なら大きい数から
INF = 1 << 60
# nx(n-1)/2通りのうちx以下の数がk個以上か判定する関数を使って、二分探索していく
def find_less_than(p, some_list):  # p以下の数がsome_listにいくつあるか
    if some_list[0] > p:
        return 0
    left = 0  # p以下の数
    right = len(some_list) - 1  # pより大きい数
    mid = (left + right) // 2
    while right - left > 2:
        if some_list[mid] > p:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid
            mid = (left + right) // 2
    return left + 1


def find_more_than(p, some_list):  # p以上の数がsome_listにいくつあるか
    if len(some_list) == 0:
        return 0
    if some_list[len(some_list) - 1] < p:
        return 0
    left = 0
    right = len(some_list) - 1
    mid = (left + right) // 2
    while right - left > 2:
        if some_list[mid] < p:
            left = mid
            mid = (right + left) // 2
        else:
            right = mid
            mid = (left + right) // 2
    return len(some_list) - right


def more_than_k_lessx(x):  # nx(n-1)/2通りのうちx以下の数がk個以上か判定する関数
    counter = 0
    for i in range(n):
        if a[i] > 0:
            counter += find_less_than(x / a[i], a[:i])
        if a[i] == 0:
            if x >= 0:
                counter += i + 1
        if a[i] < 0:
            counter += find_more_than(x / a[i], a[:i])
    return counter >= k


def main():  # nx(n-1)/2つのxのうち、x以下の数がk個以上を満たす最大のxを返す
    ng = 0
    ok = a[-1] * a[-2]
    mid = (ok + ng) // 2
    while ok - ng > 1:
        if more_than_k_lessx(mid):
            ok = mid
            mid = (ok + mid) // 2
        else:
            ng = mid
            mid = (ok + ng) // 2
    print(ok)


main()
