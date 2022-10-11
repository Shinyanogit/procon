# -*- coding: utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja
import sys
from itertools import permutations

input = sys.stdin.readline
k = int(input())
rc_list = []
for i in range(k):
    r, c = map(int, input().split())
    rc_list.append((r, c))
# 次に縦横の効きを意識してi列目のクイーンの行を格納した配列を9!通り生成
def check(queens):  # 斜めの効きを一方向について検討
    distance_list = []
    for i, j in enumerate(queens):
        if i + j not in distance_list:
            distance_list.append(i + j)
        else:
            return False
    return True


def rotate(queens):  # 右に回転
    result = [0 for i in range(8)]
    for i, j in enumerate(queens):
        result[j] = 7 - i
    return result


def check4(queens):  # 角からの距離を四角からを検討する
    queens_to_check = queens.copy()
    for i in range(4):
        if check(queens_to_check):
            queens_to_check = rotate(queens_to_check)
        else:
            return False
    return True


def show(queens):
    for column in queens:
        text = ""
        for i in range(column):
            text += "."
        text += "Q"
        for i in range(7 - column):
            text += "."
        print(text)


for queens in map(list, permutations(range(8), 8)):
    # print(queens)
    flag = True
    for r, c in rc_list:
        if queens[r] != c:
            flag = False
            break
    if not flag:
        continue
    if check4(queens):
        show(queens)
        exit()
