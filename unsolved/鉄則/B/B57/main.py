# -*- coding: utf-8 -*-
# ij成分がjに操作を2**i回行った数字を返すテーブルを作成
# なんかバグってるなぁ、、
import sys
from math import log

input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[]]
for i in range(N + 1):
    dp[0].append(i - sum(map(int, str(i))))

counter = 1
while True:
    counter *= 2
    if counter > K:  # 必要ない
        break
    answer = []
    for j in range(N + 1):
        answer.append(dp[-1][dp[-1][j]])
    dp.append(answer)
# for i in range(5):
# print(dp[i])
for i in range(1, N + 1):
    current_num = i
    for d in range(int(log(i, 2)) + 1):  # 2**d桁回目について
        if (K >> d) & 1:
            current_num = dp[d][current_num]
    print(current_num)
# print(list(range(10,31)))
# for i in range(3):
#     print(dp[i][10:31])
