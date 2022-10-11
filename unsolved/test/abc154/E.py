# -*- coding: utf-8 -*-
#
import sys, math
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


input = sys.stdin.readline
N = int(input())
K = int(input())
order = int(math.log10(N))  # 10の南条までいかにできるか
if order < K - 1:  # Nが小さすぎるレアケースについて
    count = 0
    for i in range(1, N + 1):
        if len(str(i)) - str(i).count("0") == 3:
            count += 1
    print(count)  # 多分0
    exit()
# 10**(order)未満、つまりoreder桁以下について
num = 1
# for i in range(K):  # orderCk
#     num *= order - i
#     num //= K - i
if order < K:
    num = 0
else:
    num = cmb(order, K) * (9**K)
# 10**(oreder)以上、つまりorder+1桁について
# print(num, order, K)
counter = 0
for num1 in range(1, N // (10**order) + 1):  # 最高位の数
    if K == 1:
        counter += 1
        continue
    # 二つ目以降を決定していく
    remaining_limit = N - num1 * 10**order
    for order2 in range(order):
        # print("!")
        for num2 in range(1, 10):
            if num2 * (10**order2) > remaining_limit:
                continue
            if K == 2:
                counter += 1
            # print(num1 * 10**order + num2 * 10**order2)
            # この調子で３桁目も考える
            if K == 3:
                remaining_limit2 = remaining_limit - num2 * (10**order2)
                for order3 in range(order2):
                    for num3 in range(1, 10):
                        if num3 * (10**order3) > remaining_limit2:
                            continue
                        counter += 1
                        # print(
                        # num1 * 10**order
                        # + num2 * 10**order2
                        # + num3 * 10**order3
                        # )
print(counter + num)
