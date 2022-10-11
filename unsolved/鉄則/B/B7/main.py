# -*- coding: utf-8 -*-
# また累積和。時刻iに増えた店員の数を記録しておこうO(T+N)
import sys

input = sys.stdin.readline
T = int(input())
N = int(input())
d = [0 for i in range(T + 1)]
for i in range(N):
    l, r = map(int, input().split())
    d[l] += 1
    d[r] -= 1
current_employee = 0
for di in d[:-1]:
    current_employee += di
    print(current_employee)
