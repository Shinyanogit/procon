# -*- coding: utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
import sys

input = sys.stdin.readline
n = int(input())

fib_list = [-1 for i in range(n + 1)]
fib_list[0] = 1
fib_list[1] = 1


def fib(k):
    global fib_list
    if fib_list[k] > 0:
        return fib_list[k]
    else:
        fib_list[k] = fib(k - 1) + fib(k - 2)
        return fib(k - 1) + fib(k - 2)


print(fib(n))
