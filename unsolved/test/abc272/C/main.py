# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
# 奇数足す奇数か、偶数足す偶数
N = int(input())
A = list(map(int, input().split()))
INF = 1 << 60
# odd_max,odd_semimax=-INF,-INF
# even_max,even_semimax=-INF,-INF
A = sorted(A)
A.reverse()
# odd_counter = 0
# even_counter = 0
odd = []
even = []
for a in A:
    if len(odd) + len(even) > 3:
        print(max(sum(odd), sum(even)))
        exit()
    if a % 2:
        if len(odd) > 1:
            continue
        odd.append(a)
    else:
        if len(even) > 1:
            continue
        even.append(a)
# print(odd, even)
answer = [-1]
if len(odd) == 2:
    answer.append(sum(odd))
if len(even) == 2:
    answer.append(sum(even))
print(max(answer))
