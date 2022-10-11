# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    s = input()[:-1]
    dic.setdefault(s, 0)
    dic[s] += 1
items = sorted(dic.items(), key=lambda x: x[1])
items.reverse()
trash, max_num = items[0]
results = []
for s, i in items:
    if i != max_num:
        break
    results.append(s)
for s in sorted(results):
    print(s)
