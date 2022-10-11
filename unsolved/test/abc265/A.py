# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
x, y, n = map(int, input().split())
print(min(n * x, (n // 3 * y + n % 3 * x)))
