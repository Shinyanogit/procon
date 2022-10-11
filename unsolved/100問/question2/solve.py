# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc106/tasks/abc106_b
import sys, math

input = sys.stdin.readline
n = int(input())


counter = 0
for i in range(n // 2 + 1):
    k = 2 * i + 1
    divisor_num = sum(k % i == 0 for i in range(1, k + 1))
    if divisor_num == 8:
        counter += 1
print(counter)
