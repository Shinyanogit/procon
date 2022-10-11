# -*- coding: utf-8 -*-
# 最大k回触れるとしたとき、dpだ
import sys

input = sys.stdin.readline
dp = [3.5]  # i回振れるときの期待値
N = int(input())
for i in range(N - 1):
    result = [dp[-1] for i in range(6)]
    for i in range(6, 0, -1):
        if i < dp[-1]:
            break
        result[6 - i] = i
    dp.append(sum(result) / 6)
print(dp[-1])
