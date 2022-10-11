# -*- coding: utf-8 -*-
#
import sys
from copy import copy

input = sys.stdin.readline
MOD = 10**9 + 7
n, k = map(int, input().split())
dp = [[tuple(range(n))]]
for i in range(k):
    result = dp[-1].copy()
    for case in dp[-1]:
        new_case = list(case)
        for a in range(n - 1):
            tmpa = list(case)[a]
            for b in range(a + 1, n):
                case_to_add = new_case.copy()
                print(a, b)
                tmpb = list(case)[b]
                case_to_add[a] = tmpb
                case_to_add[b] = tmpa
                result.append(tuple(case_to_add))
    dp.append(list(set((result))))
print(dp)
counter = 0
for line in dp:
    counter += 1
    print(n, counter, len(line))
