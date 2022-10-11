# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
converter = list(map(str, range(10))) + list("ABCDEF")
print(converter[N // 16] + converter[N % 16])
