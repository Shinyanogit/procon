# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0516
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
alist = [int(input()) for i in range(n)]
sum = [0]  # i成分は区間[0,i)の和
prev = 0
for i in range(n):
    prev += alist[i]
    sum.append(prev)
s_max = -float("inf")
for start in range(0, n - k + 1):  # [start,start+k)を考える
    s_max = max(s_max, sum[start + k] - sum[start])
print(s_max)
