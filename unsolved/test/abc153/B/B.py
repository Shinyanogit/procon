# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
H, N = map(int, input().split())
if sum(list(map(int, input().split()))) >= H:
    print("Yes")
else:
    print("No")
