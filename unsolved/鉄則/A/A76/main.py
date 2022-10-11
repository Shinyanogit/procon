# -*- coding: utf-8 -*-
# 特定の値より大きい値の一番左のインデックス→bisect_left
import sys
from bisect import bisect_left

MOD = 10**9 + 7
input = sys.stdin.readline
N, W, L, R = map(int, input().split())
dp = [1]  # i成分はi番目の足場まで何通りで進めるか
steps = [0] + list(map(int, input().split()))
steps.append(W)
counter = 0
dp_sum = [1]  # i成分までのdpの総和
for x in steps[1:]:
    counter += 1
    # L~Rmのジャンプで辿り着ける元の足場
    left = bisect_left(steps, x - R)
    right = bisect_left(steps, x - L + 1)
    #
    ans = 0
    # print(left, right, x - R, x - L + 1)
    if right == 0:
        dp.append(0)
        dp_sum.append(dp[-1] + dp_sum[-1])
    elif left == 0:
        dp.append(dp_sum[right - 1])
        dp_sum.append(dp_sum[counter - 1] + dp[counter])
    else:
        dp.append(dp_sum[right - 1] - dp_sum[left - 1])
        dp_sum.append(dp_sum[counter - 1] + dp[counter])
print(dp[-1])
# print(dp)
# print(dp_sum)
# print(bisect_left(steps, -7))
