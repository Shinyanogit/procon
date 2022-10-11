# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/arc054/tasks/arc054_b
# これ二分法だ
# 紆余曲折経てなんかうまく行った
import sys, math

input = sys.stdin.readline
p = float(input())
calc_time = lambda t: t + p * math.pow(2, -2 * t / 3)
dt = math.pow(10, -10)
div_calc_time = lambda t: (calc_time(t + dt) - calc_time(t - dt)) / (2 * dt)
left = 0
right = 100
mid = (left + right) / 2
while right - left > dt:
    if div_calc_time(mid) < 0:
        left = mid
        mid = (right + left) / 2
    else:
        right = mid
        mid = (right + left) / 2
print(calc_time(mid))
