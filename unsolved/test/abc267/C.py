# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
if n == m:
    print(sum([a[i] * (i + 1) for i in range(n)]))
    exit()
d = [m * a[m + 1 + i] - (m + 1) * a[m + i] + a[i] for i in range(n - m - 1)]
b = [m * a[m] - sum(a[:m])]
for d_i in d:
    b.append(b[-1] + d_i)
max_s = sum([i * a[i - 1] for i in range(1, m + 1)])
s = sum([i * a[i - 1] for i in range(1, m + 1)])
for b_i in b:
    s += b_i
    if max_s < s:
        max_s = s
print(max_s)
