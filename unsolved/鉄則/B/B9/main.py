# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
size = 1501
snow = [[0] * (size + 1) for i in range(size + 1)]
for N in range(N):
    a, b, c, d = map(int, input().split())
    snow[a][b] += 1
    snow[c][d] += 1
    snow[c][b] -= 1
    snow[a][d] -= 1
for i in range(size + 1):
    for j in range(size):
        snow[i][j + 1] += snow[i][j]
for j in range(size + 1):
    for i in range(size):
        snow[i + 1][j] += snow[i][j]
area = 0
for i in range(size):
    for j in range(size):
        if snow[i][j]:
            area += 1
print(area)
