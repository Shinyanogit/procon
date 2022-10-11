# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
H, A = map(int, input().split())
print(1 + (H - 1) // A)
