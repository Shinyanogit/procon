# -*- coding: utf-8 -*-
# 2(N-1)回の矢印を並べ替えるのは計算量的にむり
# N-1回並べ替えてスタートとゴールから合流させて(2**N-1)その後数字に一致するものがあるか(logN*2**N-1)
import sys

input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
from_start = []
start = A[0][0]
bucket_from_start = [[] for i in range(N)]


def dfs_to_the_line(value, x, y):
    if x + y == N - 1:
        bucket_from_start[x].append(value)
    else:
        # したか右に進む
        bottom_value = A[x + 1][y]
        right_value = A[x][y + 1]
        dfs_to_the_line(value ^ bottom_value, x + 1, y)
        dfs_to_the_line(value ^ right_value, x, y + 1)


dfs_to_the_line(start, 0, 0)
# ゴールから進んで一緒の値があるかどうかを返す
counter = 0
# print(bucket_from_start)


def dfs_to_the_line_from_goal(value, x, y):
    global counter
    if x + y == N:
        # print(x, value)
        counter += bucket_from_start[x - 1].count(value)
        counter += bucket_from_start[x].count(value)
        # if value in bucket_from_start[x]:
        #     counter += 1
        # else:
        #     return
    else:
        upper_value = A[x - 1][y]
        left_value = A[x][y - 1]
        dfs_to_the_line_from_goal(value ^ upper_value, x - 1, y)
        dfs_to_the_line_from_goal(value ^ left_value, x, y - 1)


dfs_to_the_line_from_goal(A[-1][-1], N - 1, N - 1)
print(counter)
