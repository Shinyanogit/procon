# -*- coding: utf-8 -*-
#
import sys


input = sys.stdin.readline
n, k = map(int, input().split())
p = list(map(int, input().split()))
S = sum(p[:k])
maxS = sum(p[:k])
for i in range(n - k):  # 動かす回数
    S += p[k + i] - p[i]
    maxS = max(maxS, S)
print((maxS + k) / 2)
