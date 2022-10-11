# -*- coding: utf-8 -*-
# アスタリスク大事、ng-ok>1
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))


def loop(r):  # K個食べるまでにr周することが可能かO(N)
    eaten = 0
    for a_i in a:
        eaten += min(a_i, r)
    return eaten <= K


# def max_roop():  # 二分探索でK個食べるまでの最大の周回回数を考えるO(NlogK)
#     ok = 0
#     ng = K + 1
#     mid = (ok + ng) // 2
#     while ng - ok > 1:
#         if loop(mid):
#             ok = mid
#             mid = (ok + ng) // 2
#         else:
#             ng = mid
#             mid = (ok + ng) // 2
#     return ok
def max_roop():  # 二分探索でK個食べるまでの最大の周回回数を考えるO(NlogK)
    ok = 0
    ng = K + 1
    mid = (ok + ng) // 2
    while ng - ok > 1:
        if loop(mid):
            ok = mid
            mid = (ok + ng) // 2
        else:
            ng = mid
            mid = (ok + ng) // 2
    return ok


roop_num = max_roop()  # Nlogk
# remain = 0
eaten = 0
for i in range(N):  # r周しておく#N
    move = min(roop_num, a[i])
    # remain += a[i] - move
    eaten += move
    a[i] -= move
# flag = True  # まだ食ってる
# ans = ""
for i in range(N):  # もう一周！
    # if flag:
    if eaten == K:
        # print(eaten)
        flag = False
        # ans += str(a[i]) + " "
        break
    if a[i]:
        # remain -= 1
        eaten += 1
        a[i] -= 1
        # ans += str(a[i]) + " "
print(*a)
