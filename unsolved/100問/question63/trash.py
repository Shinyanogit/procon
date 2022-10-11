# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc074/tasks/arc083_b
import sys

input = sys.stdin.readline
# まあ明らかにdpでしょうね
# まてよ最短経路問題で経路も考える必要があるぞ、、、ワーシャルフロイドとかダイクストラ法が有効かも、、？
n = int(input())
# dp = [float("inf") for i in range(n)]  # i成分は街0-iまでに関しての真偽
sum = 0
a = [list(map(int, input().split())) for i in range(n)]
for i in range(1, n):  # 0〜i-1までのチェックをした上でiを追加できるかと、全て経路を足し算していく
    for j in range(i):  # jからiまで
        tmp = []  # jからiまでの行き方を考える
        for k in range(j + 1):  # jからk(0-j)を経由してiまで
            tmp.append(a[j][k] + a[k][i])
        print(j, i, tmp)
        if min(tmp) == max(tmp):  # どんな新しい経路を使ってiまで行っても距離は同じ
            continue
        else:
            print(-1)
            sys.exit()
    sum += min(a[i])  # 0~i-1からiまでの最短経路
print(sum)
