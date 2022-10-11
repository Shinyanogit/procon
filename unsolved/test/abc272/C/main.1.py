# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
# 奇数足す奇数か、偶数足す偶数
N = int(input())
A = list(map(int, input().split()))
odd = []
even = []
for a in A:
    if a % 2:
        odd.append(a)
    else:
        even.append(a)
answer = [-1]
if len(odd) > 1:
    odd.sort()
    answer.append(odd[-1] + odd[-2])
if len(even) > 1:
    even.sort()
    answer.append(even[-1] + even[-2])
print(max(answer))
# print(odd, even)
