# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc034/tasks/abc034_c
import sys

input = sys.stdin.readline
MOD = pow(10, 9) + 7


def inv(n):
    return pow(n, MOD - 2, MOD)


w, h = map(int, input().split())
w -= 1
h -= 1
fact = [1]
for i in range(h + w):
    fact.append((i + 1) * fact[i] % MOD)
# print(fact, w, h)
print(fact[w + h] * inv(fact[h]) * inv(fact[w]) % MOD)
