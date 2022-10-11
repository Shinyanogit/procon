# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2017yo/tasks/joi2017yo_d
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
csum = [[0] * (N + 1) for _ in range(M)]  # ij成分は種類i(0-m-1)のぬいぐるみが位置j(0-n)におかれれいるか否か
for i in range(N):
    k = int(input())
    k -= 1
    csum[k][i + 1] = 1
#ここから先はij成分を種類iのぬいぐるみが位置0-jまでに合計何個あるかを計算
for k in range(M):
    for i in range(1, N + 1):
        csum[k][i] += csum[k][i - 1]#i,nには種類iのぬいぐるみの総数が記録されている
num = [csum[k][-1] for k in range(M)]  # k成分は位置kに置かれているぬいぐるみの種類

dp = [float("inf")] * (1 << M)  # i成分はiというフラグが立っていない範囲でうまく並び替えた時の最小数
dp[0] = 0
for S in range(1 << M):  # フラグをsとする,これに則った種類のぬいぐるみを左からならべる
    tot = 0
    for x in range(M):
        if S & 1 << x:  # sのうちx番目が立っている(種類xを固定)
            tot += num[x]  # 固定したぬいぐるみの総数
    # ここまで読んだ、難しすぎんか
    for x in range(M):
        if not S & 1 << x:#種類xは動かす
            dp[S ^ 1 << x] = min(
                dp[S ^ 1 << x], dp[S] + num[x] - csum[x][tot + num[x]] + csum[x][tot]
            )#種類xを動かさない場合の通りは、
print(dp[-1])
