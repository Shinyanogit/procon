# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline

N, R = map(int, input().split())
if N < 10:
    print(R - 100 * N + 1000)
else:
    print(R)
