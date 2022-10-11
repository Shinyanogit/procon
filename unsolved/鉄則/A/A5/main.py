# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n, k = map(int, input().split())


def nCk(n, k):
    bunshi = 1
    bunbno = 1
    for i in range(k):
        bunbo *= i + 1
        bundhi *= n - i
    return bunshi / bunbno


if k > 3 * n:
    print(0)
    exit()
counter = 0
# for a in range(1, min(n, k // 3)):
#     if (k - a) // 2 >= a:
#         counter += (k - a) // 2 - a + 1
#     print(a, (k - a) // 2 - a + 1)
for a in range(1, min(k - 1, n + 1)):
    for b in range(1, min(k - a, n + 1)):
        if 1 <= (k - a - b) <= n:
            counter += 1

print(counter)
