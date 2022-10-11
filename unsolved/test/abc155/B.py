# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
for a_i in a:
    if a_i % 2 or a_i % 3 == 0 or a_i % 5 == 0:
        continue
    print("DENIED")
    exit()
print("APPROVED")
