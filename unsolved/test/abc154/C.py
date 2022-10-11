# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
if len(set(a)) == N:
    print("YES")
else:
    print("NO")
