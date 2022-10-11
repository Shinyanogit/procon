# -*- coding: utf-8 -*-
#
import sys

# 多分dpだろ知らんけど
# 模範解答だとまず解決する課題の組み合わせを決めて、締め切り順に処理するらしい、でもNlogNなんだよなぁ、、あ、小課題２までだよねやっぱ
# ソートしてから、i日目までにj番目までの仕事を好きなように選んで点数を最大化するテーブルを考えよう！（logN+DxN）
# 漸化式の立て方に頭を使う、けど計算量的に漸化式立てるしかない
input = sys.stdin.readline
N = int(input())
tasks = []
dmax = 0
for i in range(N):
    d, c, s = map(int, input().split())
    dmax = max(dmax, d)
    tasks.append((d, c, s))
tasks.sort()
INF = 1 << 60
dp = [[0] * (N + 1) for i in range(dmax + 1)]
# dp[i][j]=max(dp[i][j-1],dp[i-)
for i in range(1, dmax + 1):  # i日目までに着いて
    for j in range(1, N + 1):  # j番目までの仕事を考える
        dj, cj, sj = tasks[j - 1]
        if i >= cj and i <= dj:  # 仕事jが達成可能
            dp[i][j] = max(dp[i][j - 1], dp[i - cj][j - 1] + sj)
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[-1][-1])
# for i in range(dmax + 1):
# for j in range(N + 1):
# print(i, j, " ", dp[i][j])
