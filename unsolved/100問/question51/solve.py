# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_d
import sys

input = sys.stdin.readline
MOD = 10007
# どうせまたdpでしょ、、、
# 今回はi日目での出席の取り方が、i-1日目の出席者に左右される
n = int(input())
presidents = list(input()[:-1])
dp = []  # i成分はi日目までのスケジュールの全通りを表していている,ただしJ,O,Iが出席したかどうかで場合分けしてj,k,l成分に格納する
# 初日は手入力
president0 = presidents[0]
result = [[[0] * 2 for o in range(2)] for j in range(2)]
get_name_by_id = [[[""] * 2 for o in range(2)] for j in range(2)]
for j in range(2):
    for o in range(2):
        for i in range(2):
            if j:
                get_name_by_id[j][o][i] += "J"
            if o:
                get_name_by_id[j][o][i] += "O"
            if i:
                get_name_by_id[j][o][i] += "I"
# print(get_name_by_id)
if president0 == "J":  # J君が責任者で、ioの出席は任意
    for o in range(2):
        for i in range(2):
            result[1][o][i] = 1
elif president0 == "O":
    for j in range(1, 2):
        for i in range(2):
            result[j][1][i] = 1
else:
    for j in range(1, 2):
        for o in range(2):
            result[j][o][1] = 1
dp.append(result)

for l in range(n - 1):  # i日目の情報をもとにi+1日目を考える
    president = presidents[l + 1]  # 以下presidentを含む要素を全て足していく
    prev_day = dp[-1]
    tmp = [[[0] * 2 for o in range(2)] for i in range(2)]
    for j in range(2):
        for o in range(2):
            for i in range(2):
                name = get_name_by_id[j][o][i]  # 当日の出席
                if president in name:  # presidentが出席時のみ、dp[i+1][j][o][i]を計算していく
                    for prev_j in range(2):
                        for prev_o in range(2):
                            for prev_i in range(2):
                                if (
                                    (j * prev_j) + (o * prev_o) + (i * prev_i)
                                ):  # 鍵の受け渡しが可能だった
                                    tmp[j][o][i] += prev_day[prev_j][prev_o][prev_i]
                                    tmp[j][o][i] %= MOD
                                    # print(
                                    #     get_name_by_id[prev_j][prev_o][prev_i],
                                    #     get_name_by_id[j][o][i],
                                    #     prev_day[prev_j][prev_o][prev_i],
                                    # )
                                    # if get_name_by_id[j][o][i] == "JOI":
                                    # print(
                                    #     "plus",
                                    #     prev_day[prev_j][prev_o][prev_i],
                                    #     tmp[j][o][i],
                                    # )
    dp.append(tmp)
totnum = 0
for j in range(2):
    for o in range(2):
        for i in range(2):
            totnum += dp[-1][j][o][i]
print(totnum % MOD)
