# -*- coding: utf-8 -*-
#
import sys
from collections import deque

input = sys.stdin.readline
Q = int(input())
S = deque()
for i in range(Q):
    query = input()[:-1].split()
    if query[0] == "1":
        S.append(query[1])
    elif query[0] == "2":
        print(S[-1])
    else:
        S.pop()
