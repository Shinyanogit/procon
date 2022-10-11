# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/arc054/tasks/arc054_b
import sys, math

input = sys.stdin.readline
dt = math.pow(10, -10)
p = float(input())
calc_time = lambda start: p * math.pow(2, -start * 2 / 3) + start
division = lambda start: (calc_time(start + dt) - calc_time(start - dt)) / (2 * dt)
left = 0
right = p
mid = p / 2
while right - left > dt:
    # print(left, right)
    if division(mid) < 0:
        left = mid
        mid = (right + left) / 2
    else:
        right = mid
        mid = (left + right) / 2
print(calc_time(mid))
