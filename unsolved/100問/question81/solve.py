# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc014/tasks/abc014_3
import sys

input = sys.stdin.readline
# 目的はa(i成分が濃さがiの絵の具の人気度合い)という配列を手に入れること
# 各区間について＋１を繰り返すと計算量はO(O(1000000xn)つまり無理
# aの階差数列dを考えてみる
n = int(input())
a0 = 0  # 色0の人気
d = [0 for i in range(10**6)]  # i(0-10**6-1)成分はai+1-ai
for i in range(n):
    a, b = map(int, input().split())
    if a >= 1:
        d[a - 1] += 1
    else:
        a0 += 1
    if b < 10**6:
        d[b] -= 1
max_popularity = a0
for i in range(10**6):  # 色i+1をiをもとに考える
    a0 += d[i]
    max_popularity = max(max_popularity, a0)
print(max_popularity)
