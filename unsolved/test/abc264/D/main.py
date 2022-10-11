# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
answer = 0
S = list(input()[:-1])
for cha in "atcoder":
    answer += S.index(cha)
    S.remove(cha)
print(answer)
