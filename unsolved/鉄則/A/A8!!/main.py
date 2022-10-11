# -*- coding: utf-8 -*-
# にもす法（二次元累積話だ）
# 要するに(0,0)と(h,w)を対角線の２端点とする長方形内の総和が求まればよい
# エッジケースに注意
import sys

input = sys.stdin.readline
H, W = map(int, input().split())
a = [list(map(int, input().split())) for i in range(H)]
S = a.copy()


def show():
    for line in S:
        print(line)
    print()


# show()
for i in range(0, H):
    for j in range(1, W):
        S[i][j] = S[i][j] + S[i][j - 1]
# show()
for j in range(0, W):
    for i in range(1, H):
        S[i][j] += S[i - 1][j]
# show()


def answer(a, b, c, d):
    # print(S[c][d] + S[a][b] - S[a][d] - S[b][c])
    # print(Sum(c, d), Sum(a - 1, b - 1), Sum(a - 1, d), Sum(c, b - 1))
    print(Sum(c, d) + Sum(a - 1, b - 1) - Sum(a - 1, d) - Sum(c, b - 1))


def Sum(i, j):
    if (i + 1) * (j + 1):
        return S[i][j]
    return 0


Q = int(input())
for i in range(int(Q)):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    answer(a, b, c, d)
