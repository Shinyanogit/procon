# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
a0 = a[0]
S = [a0]
# print(a, n, p, q, r)
for i in range(n - 1):
    a0 += a[i + 1]
    S.append(a0)


def sum(x, y):  # x番目からy番目までの和
    if x == 0:
        return S[y]
    return S[y] - S[x - 1]


for x in range(n):
    left = 0
    right = n+1
    y = (left + right) // 2
    while right - left > 1:
        # print(left, right)
        if sum(x, y - 1) > p:
            right = y
            y = (left + right) // 2
        else:
            left = y
            y = (left + right) // 2
    if sum(x, y - 1) != p:
        continue
    left = y
    right = n+1
    z = (left + right) // 2
    while right - left > 1:
        if sum(y, z - 1) > q:
            right = z
            z = (left + right) // 2
        else:
            left = z
            z = (left + right) // 2
    if sum(y, z - 1) != q:
        continue
    left = z
    right = n+1
    w = (left + right) // 2
    while (right - left) > 1:
        if sum(z, w - 1) > r:
            right = w
            w = (left + right) // 2
        else:
            left = w
            w = (left + right) // 2
    if sum(z, w - 1) != r:
        continue
    print("Yes")
    exit()
print("No")
