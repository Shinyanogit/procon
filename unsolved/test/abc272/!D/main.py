# -*- coding: utf-8 -*-
# 幅優先探索かなぁ
import sys
from math import sqrt
from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())
root_M = int(sqrt(M / 2))
# まずは平方和がMとなる２数の組み合わせを考える
vector = set()
for i in range(root_M + 1):
    if int(sqrt(M - i**2)) == sqrt(M - i**2):
        vector.add((i, int(sqrt(M - i**2))))
        vector.add((i, -int(sqrt(M - i**2))))
        vector.add((-i, int(sqrt(M - i**2))))
        vector.add((-i, -int(sqrt(M - i**2))))
        vector.add((int(sqrt(M - i**2)), i))
        vector.add((int(sqrt(M - i**2)), -i))
        vector.add((-int(sqrt(M - i**2)), i))
        vector.add((-int(sqrt(M - i**2)), -i))
# print(vector)
INF = 1 << 20
find_next = deque()
find_next.append((0, 0, 0))
dp = [[-1] * N for i in range(N)]
dp[0][0] = 0
# print(find_next.pop())
while find_next:
    steps, x, y = find_next[0]
    find_next.popleft()
    # if (x,y)==(i,j)
    # print(x, y, "Position")
    for p, q in vector:
        # print(p, q, "Vector")
        if not (0 <= x + p < N and 0 <= y + q < N):
            # print(36)
            continue
        if dp[x + p][y + q] == -1:
            dp[x + p][y + q] = steps + 1
            find_next.append((steps + 1, x + p, y + q))
for line in dp:
    print(*line)
