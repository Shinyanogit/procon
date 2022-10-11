# -*- coding: utf-8 -*-
#  
import sys

input = sys.stdin.readline
# dpで解けそう
dp = [[]]  # i成分はi番目までの部分数列に対して色を塗り分けた時の各色の最大値リスト
n = int(input())
a_list = [int(input()) for i in range(n)]
dp[0] = [a_list[0]]
for a in a_list[1:]:
    if min(dp[-1])<=a
