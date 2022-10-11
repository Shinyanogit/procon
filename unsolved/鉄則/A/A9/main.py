# -*- coding: utf-8 -*-
# エッジケースに気を付ける
import sys


def show():
    for line in snow[:-1]:
        print(*line[:-1])


input = sys.stdin.readline
H, W, N = map(int, input().split())
snow = [[0] * (W + 1) for i in range(H + 1)]
for i in range(N):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    snow[a][b] += 1
    snow[c + 1][d + 1] += 1
    snow[a][d + 1] -= 1
    snow[c + 1][b] -= 1
# show()
# print()
for i in range(H):
    # for i in range(H + 1):
    for j in range(W - 1):
        snow[i][j + 1] += snow[i][j]
# show()
# print()
for j in range(W):
    # for j in range(W + 1):
    for i in range(H - 1):
        snow[i + 1][j] += snow[i][j]
show()
