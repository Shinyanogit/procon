# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
a, b = map(int, input().split())
counter = 0
point = 1
for i in range(3):
    if a % 2 or b % 2:
        counter += point
    point *= 2
    a //= 2
    b //= 2
print(counter)
