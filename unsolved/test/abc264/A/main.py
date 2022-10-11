# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
L, R = map(int, input().split())
print("atcoder"[L - 1 : R])
