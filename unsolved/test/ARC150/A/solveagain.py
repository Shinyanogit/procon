# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
T = int(input())


def main(N, K, S):
    tot_one = 0
    counter_available = 0
    for s in S:
        if s == "1":
            tot_one += 1
    # 先頭がi番目の時のK個の文字列の中に1,0がいくつあるのかを調べ、0の数か0個であること、かつ1の数が最大であることが達成されているかを判定する
    # まずは先頭が0となるとき
    count_0 = 0
    count_1 = 0
    for i in range(K):
        if S[i] == "0":
            count_0 += 1
        elif S[i] == "1":
            count_1 += 1
    if count_0 == 0 and count_1 == tot_one:
        counter_available += 1
    for head in range(1, N - K + 1):
        if S[head - 1] == "1":
            count_1 -= 1
        elif S[head - 1] == "0":
            count_0 -= 1
        if S[head + K - 1] == "1":
            count_1 += 1
        elif S[head + K - 1] == "0":
            count_0 += 1
        if count_0 == 0 and count_1 == tot_one:
            counter_available += 1
    if counter_available == 1:
        print("Yes")
    else:
        print("No")


for i in range(T):
    N, K = map(int, input().split())
    S = input()[:-1]
    main(N, K, S)
