# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1
import sys

input = sys.stdin.readline
n = int(input())
lights = list(map(int, input().split()))
for i in range(0, n, 2):
    lights[i] = (lights[i] + 1) % 2
# あとはlightsを1か０に統一すればよろしい
line = []  # 連続した長さを放り込んでいく
prev_num = -1
for num in lights:
    if num != prev_num:
        line.append(1)
        prev_num = num
    else:
        line[-1] += 1
        prev_num = num
# 連続した部分を任意に一つ連結する
max_num = 0
if len(line) < 3:
    print(len(lights))
    exit()
for i in range(len(line) - 2):
    score = line[i] + line[i + 1] + line[i + 2]
    max_num = max(max_num, score)
print(max_num)
