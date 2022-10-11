# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# まーたメモリ制限だよ、、、
# bisect使わないとダメっぽい
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
score1 = [int(input()) for i in range(n)] + [0]
score2 = []
# まず２本のダーツで取れる点数を列挙する(O(n²))
for score_a in score1:
    for score_b in score1:
        sum = score_a + score_b
        if sum <= m:
            score2.append(sum)
score2.sort()
size = len(score2)


def calc_max(score12):
    global size, score2
    left = 0
    right = size - 1
    mid = (left + right) // 2
    while right - left > 1:
        if score2[mid] + score12 > m:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid
            mid = (right + left) // 2
    return score2[mid] + score12


max_sum = 0
# 2回の点数がscore12であった時の残りの2本の点数の撮り方のうち、総合点がm以下最大になるものを各々算出し(O(n²xlogn))、その最大値を算出する
for score12 in score2:
    max_sum = max(calc_max(score12), max_sum)
print(max_sum)
