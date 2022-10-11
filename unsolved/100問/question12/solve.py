# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc002/tasks/abc002_4
import sys

# 全探索でも解けるけど、後学のためにダイクストラ法で考えてみる
# うまくいかないしいいや
input = sys.stdin.readline
n, m = map(int, input().split())
grouped = [1 for i in range(n)]
commorades = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    commorades[a].append(b)
    commorades[b].append(a)


def make_group(i):
    global grouped, commorades
    size = 1
    grouped[i] = 0
    seach_list = commorades[i].copy()
    print(i)
    for friend in seach_list:
        if grouped[friend]:
            # print(friend)
            size += make_group(friend)
    return size


max_size = 0
for i in range(n):
    if grouped[i]:  # まだiが仲間に入ってない
        size = make_group(i)
        if size > max_size:
            max_size = size
    print("-------")
print(max_size)
