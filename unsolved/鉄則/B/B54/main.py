# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
counter = {}
Sum = 0
for i in range(N):
    a = int(input())
    counter.setdefault(a, 0)
    counter[a] += 1
    Sum += counter[a] - 1
print(Sum)
