# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n = int(input())
# ルークのない行と列を別々に求めればOK
# 二分探索！！！
# まず縦から
# flushとエッジケースを忘れずに
def ask(a, b, c, d):
    print(f"? {a} {b} {c} {d}", flush=True)
    # print()
    T = int(input())
    if T == -1:
        exit()
    return T


def find_row():
    upper = 1
    bottom = n
    mid = (upper + bottom) // 2
    while bottom - upper > 0:
        if ask(upper, mid, 1, n) == mid - upper + 1:
            upper = mid + 1
            mid = (upper + bottom) // 2
        else:
            bottom = mid
            mid = (bottom + upper) // 2
    return mid


def find_column():
    left = 1
    right = n
    mid = (left + right) // 2
    while right - left > 0:
        if ask(1, n, left, mid) == mid - left + 1:
            left = mid + 1
            mid = (left + right) // 2
        else:
            right = mid
            mid = (left + right) // 2
    return mid


row = find_row()
column = find_column()
print(f"! {row} {column}", flush=True)
