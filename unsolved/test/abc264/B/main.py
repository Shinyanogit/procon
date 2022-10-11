# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
x, y = abs(R - 8), abs(C - 8)
if max(x, y) % 2:
    print("black")
else:
    print("white")
