# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
# ij成分が0~i行、0~j列の総和になるような配列を累積和で求めるよう
# あ、だめじゃん
n, m = map(int, input().split())


def answer(a, b, c, d):
    print(a, b, c, d)
    # ijが奇数
    a1 = a // 2 + 1
    b1 = (b + 1) // 2
    c1 = c // 2 + 1
    d1 = (d + 1) // 2
    sum1 = (d1**2 - (c1 - 1) ** 2) * m + ((b1**2 - (a1 - 1) ** 2) // 2)
    # ijが偶数
    c2 = (c + 1) // 2
    d2 = d // 2
    a2 = (a + 1) // 2
    b2 = b // 2
    sum2 = b2 * (b2 + 1) - (a2 - 1) * a2 + m * (d2 * (d2 + 1) - c2 * (c2 - 1)) // 2
    print(sum1, "  ", sum2)
    return sum1 + sum2


q = int(input())
for i in range(q):
    a, b, c, d = map(int, input().split())
    print(answer(a, b, c, d))
