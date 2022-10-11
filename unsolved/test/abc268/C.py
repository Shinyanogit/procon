# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
# Nを二進数表示して、1となるくらいを前列挙しaというリストに格納
# その後a_iのくらいの数を1とするかどうか一つ一つ検討する.
N2 = str(bin(N))[2:]
# print(N2[2:])
# print(type(N2))
N2 = list(N2)
N2.reverse()
# print(N2)
a = []
for i in range(len(N2)):
    if N2[i] == "1":
        a.append(i)
size = len(a)
# print(a)
for i in range(2 ** size):
    sum_i = 0
    for j in range(size):
        if (i >> j) % 2:
            sum_i += 2 ** a[j]
    print(sum_i)
