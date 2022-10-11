# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
a, b, c = sorted(list(map(int, input().split())))
if a == b and b != c or a != b and b == c:
    print("Yes")
else:
    print("No")
