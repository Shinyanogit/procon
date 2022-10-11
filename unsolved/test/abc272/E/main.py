# -*- coding: utf-8 -*-
# 0からNまでの間に必ず答えはある
# 各の数字について、0~Nになりうる場合を、その試行回数とそのときの数字を同時に記録しておくO(N*logN)
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
# 各数字にいつ邪魔しに来るのかインタビューする
found_sets = [set() for i in range(M)]
for i, a in enumerate(A):
    start = (-a - 10) // (i + 1) - 10
    goal = (-a + 10) // (i + 1) + 10
    # print(start, goal)
    for j in range(start, goal):
        # print(0, j, M, a + (i + 1) * j)
        if not (0 < j <= M):
            # print(17)
            continue
        if 0 <= a + (i + 1) * j <= N:
            # print(20, a - (i + 1) * j)
            found_sets[j - 1].add(a + (i + 1) * j)
# print(found_sets)
for s in found_sets:
    for i in range(N + 1):
        if i in s:
            continue
        print(i)
        break
