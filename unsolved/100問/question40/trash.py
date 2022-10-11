# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
# 初日のパスタが0で決まっていて、その後からi(0-)日間が空白で、その後のパスタが決定している時のパスタの通りを計算する
# なおこのコードは3日を２日と勘違いしたバカによるコードです
dp = [[0, 1, 1] for i in range(n)]  # ij成分は間がi日、jが種類
for i in range(1, n):
    n0, n1, n2 = dp[i - 1]
    N0, N1, N2 = n1 + n2, n0 + n2, n0 + n1
    dp[i] = [N0, N1, N2]
same = [pasta[0] for pasta in dp]  # 最初と最後が一緒で間がi日の時のパスタの総数
different = [pasta[1] for pasta in dp]
print(same, different)
pasta_data = []
for i in range(k):
    day, pasta = map(int, input().split())
    day -= 1
    pasta -= 1
    pasta_data.append((day, pasta))
pasta_data.sort()
result = 0  # 最初と最後を9通り変動させて集計
for i in range(3):
    flag = False
    prev_day, prev_pasta = (0, i)  # 初日のパスタがi
    sum1 = 1
    for Pasta in pasta_data:
        day, pasta = Pasta
        aida = day - prev_day - 1
        if aida >= 0:  # 日にちが一致しない
            if pasta == prev_pasta:  # パスタが一致
                sum1 *= same[aida]
                print("x", same[aida])
            else:  # パスタが違う
                sum1 *= different[aida]
                print("x", aida)
        else:  # 間が-1日（やばい）
            if pasta != prev_pasta:
                flag = True
                break
        prev_day = day
        prev_pasta = pasta
    if flag:  # やり直し
        continue
    # 最終日のパスタがj
    for j in range(3):
        sum2 = 1
        day, pasta = (n - 1, j)
        aida = day - prev_day
        if aida >= 0:  # 日にちが不一致
            if pasta == prev_pasta:  # パスタが一致
                sum2 *= same[aida]
                print("x", same[aida])
            else:  # パスタが違う
                sum2 *= different[aida]
                print("x", different[aida])
        else:  # 間が-1日（やばい）
            if pasta != prev_pasta:
                flag = True
                continue
        print(i, j, sum1, sum2, aida, result)
        result += sum1 * sum2
print(result)
