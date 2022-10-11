# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
import sys

# dpっぽい、i列目までの色をもとにi+1列目までの塗り方を変える感じなのかな

input = sys.stdin.readline
n = int(input())
columns = [[0, 0, 0, 0, 0] for i in range(n)]  # 各列の色を表す数字を格納


def switch_colour_to_num(colour):
    if colour == "R":
        return 0
    elif colour == "B":
        return 1
    elif colour == "W":
        return 2
    else:  # ゴミ
        return -1


dp = [[0, 0, 0] for i in range(n)]  # i成分はi列目までで最後の行が赤、青、白となるように塗り替えるための手数のうち、最小の手数
for i in range(5):
    colours = list(input()[:-1])
    counter = 0
    for colour in colours:
        columns[counter][i] = switch_colour_to_num(colour)
        counter += 1


def calc_cost(column, colour):  # columnをcolourが0なら赤、1で青,2で白に塗り替えるためのコスト
    cost = 0
    for number in column:
        if number != colour:
            cost += 1
    return cost


first_column = columns[0]
black = 0
blue = 0
red = 0
white = 0
for num in first_column:
    if num == 0:
        red += 1
    elif num == 1:
        blue += 1
    elif num == 2:
        white += 1
    else:
        black += 1
dp[0] = [blue + white + black, red + white + black, red + blue + black]  # 初項を与えてあげる
for i in range(n - 1):  # 1列目からn-1列目まで前の項をもとに計算していく
    red, blue, white = dp[i]
    new_red = calc_cost(columns[i + 1], 0) + min(blue, white)
    new_blue = calc_cost(columns[i + 1], 1) + min(red, white)
    new_white = calc_cost(columns[i + 1], 2) + min(blue, red)
    dp[i + 1] = [new_red, new_blue, new_white]
print(min(dp[-1]))
