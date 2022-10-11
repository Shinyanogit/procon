# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc145/tasks/abc145_d
import sys

input = sys.stdin.readline
MOD = (10**9) + 7
x, y = map(int, input().split())
step = (x + y) // 3
left = x - step
if (x + y) % 3 or x / y > 2 or y / x > 2:
    # print("unreachable")
    print(0)
    exit()


def inv(n):
    return pow(n, MOD - 2, MOD)


fact = [1]
for i in range(step):
    fact.append((fact[i] * (i + 1)) % MOD)
print(fact[step] * inv(fact[left]) * inv(fact[step - left]) % MOD)
