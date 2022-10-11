# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
from collections import deque

S = deque()
Q = int(input())
for i in range(Q):
    query = input()[:-1].split()
    if query[0] == "1":
        S.append(query[1])
        continue
    if query[0] == "2":
        print(S[0])
        continue
    if query[0] == "3":
        S.popleft()
        continue
