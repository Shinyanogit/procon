# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b
# 普通にやると計算量はO(n*2**n)
# まず適当にスタートを決めることで一列にして、それにdpを適応すればO(n²)でたえ、、、ない！n<10**9とりあえず実装はしてみる
import time

s = time.time()
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
cake2 = [int(input()) for i in range(n)] * 2
max_piece_dp = [[-1] * 2 * n for i in range(2 * n)]  # ij成分は区間[i,j)の最大値
for i in range(2 * n):
    max_piece_dp[i][i] = 0  # 区間が潰れたら0になるように初期設定


def dp(l, r):  # 区間[i,j)をとりあう時の最大値を返す関数
    # 考察済み
    # print(l, r, n)
    if max_piece_dp[l][r] >= 0:
        ans = max_piece_dp[l][r]
    # 以降は計算が必要
    elif (n - r + l) % 2:  # 残り数の偶奇がnと不一致で、初手がIOIちゃん
        if cake2[l] < cake2[r - 1]:
            # 右側はIOIが取る
            ans = dp(l, r - 1)
            max_piece_dp[l][r] = ans
        else:
            ans = dp(l + 1, r)
            max_piece_dp[l][r] = ans
    else:  # 残り数の偶奇がnと一致し初手がJOIくん
        ans = max(dp(l + 1, r) + cake2[l], dp(l, r - 1) + cake2[r - 1])
        max_piece_dp[l][r] = ans
    return ans


max_result = 0
for start in range(n):  # 区間は[start,start+n)
    tmp = dp(start, start + n)
    if tmp > max_result:
        max_result = tmp
print(max_result)
print(time.time() - s)
