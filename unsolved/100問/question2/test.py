# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc106/tasks/abc106_b
import sys, math

# なぜかうまくいかない
# input = sys.stdin.readline
# n = int(input())

for n in range(1000):
    counter = 0
    for i in range(n // 2 + 1):
        k = 2 * i + 1
        divisor_num = sum(k % i == 0 for i in range(1, k + 1))
        if divisor_num == 8:
            c = 0
            for j in [k % i == 0 for i in range(1, k + 1)]:
                c += 1
                if j:
                    print(c, n)
            counter += 1
    ans1 = counter

    ans = 0
    for n in range(1, n + 1, 2):
        sm = sum(n % i == 0 for i in range(1, n + 1))
        if sm == 8:
            ans += 1
    ans2 = ans
    if ans1 != ans2:
        print(n, ans1, ans2)
        break
