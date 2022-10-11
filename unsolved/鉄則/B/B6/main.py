# -*- coding: utf-8 -*-
# 0つ目からn爪までの間のアタリーハズレを格納するテーブルを作ろう
import sys

input = sys.stdin.readline
N = int(input())
S = [0]
for a in list(map(int, input().split())):
    if a:
        S.append(S[-1] + 1)
    else:
        S.append(S[-1] - 1)
for i in range(int(input())):
    l, r = map(int, input().split())
    result = S[r] - S[l - 1]
    if result > 0:
        print("win")
    elif result == 0:
        print("draw")
    else:
        print("lose")
