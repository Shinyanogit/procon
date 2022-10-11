# -*- coding: utf-8 -*-
#
import sys
from collections import deque

input = sys.stdin.readline
N, X = map(int, input().split())
search_que = deque([X - 1])
A = list(input()[:-1])
A[X - 1] = "@"
while search_que:
    x = search_que.popleft()
    if 0 <= x - 1:
        if A[x - 1] == ".":
            A[x - 1] = "@"
            search_que.append(x - 1)
            # print(x - 1, A)
    if x + 1 <= N - 1:
        if A[x + 1] == ".":
            A[x + 1] = "@"
            search_que.append(x + 1)
            # print(x + 1, A)
print("".join(A))
