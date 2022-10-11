# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
x, y, z = map(int, input().split())
if x * y < 0 or y / x > 1:
    print(abs(x))
    exit()
else:
    if y / z > 1:
        print(abs(x))
    elif z * y < 0:
        print(2 * abs(z) + abs(x))
    else:
        print(-1)
        exit()
