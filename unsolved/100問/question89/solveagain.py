# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1
import sys

input = sys.stdin.readline
n = int(input())
illumination = list(map(int, input().split()))
# あらかじめ点灯させておく
for i in range(n):
    if i % 2:
        illumination[i] += 1
        illumination[i] %= 2
# ここから任意の一列を点灯させて1か0の列を作ることを考える
line = []
prev_light = -1
for light in illumination:
    if prev_light != light:
        line.append(1)
    else:
        line[-1] += 1
    prev_light = light
# print(illumination)
# print(line)
max_length = 0
if len(line) < 3:
    print(len(illumination))
    exit()
# 反転させる区画をiとする
for i in range(len(line) - 2):
    max_length = max(max_length, line[i] + line[i + 1] + line[i + 2])
print(max_length)
