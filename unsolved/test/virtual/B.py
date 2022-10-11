# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc268/tasks/abc268_b
import sys

input = sys.stdin.readline
S = input()[:-1]
T = input()[:-1]
if S == T[: len(S)]:
    print("Yes")
else:
    print("No")
