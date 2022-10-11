# -*- coding: utf-8 -*-
# /Users/shinyyama/Documents/python/kyoupro/unsolved/100問/question74
import sys

MOD = 10**9 + 7

input = sys.stdin.readline
n = int(input())
k = int(input())
# from itertools import combinations

# print(len(list(combinations(range(n + k - 1), k))))
from math import factorial


def multi_from_a_to_b(a, b):
    result = 1
    for i in range(a, b + 1):
        result *= i
    return result


# ans = int(factorial(n + k - 1) / (factorial(n - 1) * factorial(k)))
ans = int(multi_from_a_to_b(n, n + k - 1) // factorial(k))
answer = ans % MOD
print(answer)
