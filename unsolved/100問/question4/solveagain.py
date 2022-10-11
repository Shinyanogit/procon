# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# 曲を全組試すと計算量はO(m²n)いける
a = [list(map(int, input().split())) for i in range(n)]  # ij成分はiくんが曲jを歌った時の得点
max_score = 0
for song1 in range(m):
    for song2 in range(song1 + 1, m):
        score = 0
        for i in range(n):
            score += max(a[i][song1], a[i][song2])
        if score > max_score:
            max_score = score
print(max_score)

