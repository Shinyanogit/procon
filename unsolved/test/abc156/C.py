# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
mean = int(sum(X) / N)
Sum1 = 0
Sum2 = 0
for x in X:
    Sum1 += (x - mean) ** 2
    Sum2 += (x - mean - 1) ** 2
print(min(Sum1, Sum2))
