# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
H_list = list(map(int, input().split()))
H_list.sort()
counter = 0
if K >= N:
    print(0)
    exit()
for i in range(N - K):
    H = H_list[i]
    counter += H
print(counter)
