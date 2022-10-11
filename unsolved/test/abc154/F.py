# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
MOD = 10**9 + 7
from operator import mul
from functools import reduce

r1, c1, r2, c2 = map(int, input().split())
n = r2 + c2 + 100
fact = [1 for _ in range(n + 1)]
inv = [1 for _ in range(n + 1)]
factinv = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    factinv[i] = (factinv[i - 1] * inv[i]) % MOD


def cmb(n, r):
    return fact[n] * factinv[r] * factinv[n - r] % MOD


def area(c, r):
    return cmb(r + c + 2, r + 1) - 1


print((area(r2, c2) - area(r2, c1 - 1) - area(r1 - 1, c2) + area(r1 - 1, c1 - 1)) % MOD)

# for i in range(10):
#     string = []
#     for j in range(10):
#         string.append(area(i, j))
#     print(string)
