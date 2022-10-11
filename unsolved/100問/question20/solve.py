# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc077/tasks/arc084_a
import sys

input = sys.stdin.readline
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
a_list.sort()
b_list.sort()
c_list.sort()
# 各bに対して、a,cの選び方を考える
import bisect


sum = 0
for b in b_list:
    a_num = bisect.bisect_left(a_list, b)  # b未満のaの個数
    c_num = len(c_list) - bisect.bisect_right(c_list, b)  # bより大きいcの個数
    sum += a_num * c_num
print(sum)
