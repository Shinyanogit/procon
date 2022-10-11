# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
s, t = input()[:-1].split()
a, b = map(int, input().split())
u = input()[:-1]
if u == s:
    print(f"{a-1} {b}")
elif u == t:
    print(f"{a} {b-1}")
else:
    print(s, " ", t, " ", u, len(s), len(t), len(u))
