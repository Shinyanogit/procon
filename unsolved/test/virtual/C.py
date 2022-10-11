# まず料理を3組作って一列に並べるのが丸そう
# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n = int(input())
p_list = list(map(int, input().split()))
p_list = p_list.copy() + p_list.copy() + p_list.copy()
# print(p_list)
# 最初0人目は0番目の料理の正面にいて、そこからiずれて1+i番目の料理に対面する
# j番目の料理が出た時にその料理が喜ばれる回転成分の票数を+1する
popularity_list = [0 for i in range(3 * n)]
for i, p in enumerate(p_list):
    for a in [i - p - 1, i - p, i - p + 1]:
        if a >= 0 and a < 3 * n:
            popularity_list[a] += 1
max_popularity = 0
for poppularity in popularity_list[: n + 1]:
    if max_popularity < poppularity:
        max_popularity = poppularity
print(max_popularity)
