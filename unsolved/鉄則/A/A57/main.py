# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
f = lambda s: int(s) - 1
A = list(map(f, input().split()))
# print(A)
# 二進数表記すればlogN回の計算で終了
# まずは1,2,4,8,,,,,(10**9以下の2の累乗)日語についてそれぞれどこに位置するかを記録していくO(Nlog10**9)
dp = [A]  # ni成分は2**n日後のアリiの位置
day = 2
while day <= 10**9:
    answer = [0 for i in range(N)]
    for i in range(N):
        # print(dp)
        answer[i] = dp[-1][dp[-1][i]]
        # print(dp[-1][dp[-1][i]], 19)
        # print(answer[i], 20)
    day *= 2
    dp.append(answer)
# for line in dp:
# print(line)
max_order = len(dp)
for i in range(Q):
    X, Y = map(int, input().split())
    # print(X, Y)
    current_place = X - 1
    for d in range(max_order, -1, -1):
        if ((Y >> d) & 1) == 1:  # Yの2**d桁目が1であった場合
            # print(d)
            current_place = dp[d][current_place]
    print(current_place + 1)
    # print()
