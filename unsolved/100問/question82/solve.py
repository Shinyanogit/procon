# -*- coding: utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2013
import sys

input = sys.stdin.readline
# これいもす法だ


def change_time_to_sec(text):
    h, m, s = map(int, text.split(":"))
    return h * 3600 + m * 60 + s


def main():
    n = int(input())
    if n == 0:
        exit()
    div_train_num = [0 for i in range(24 * 3600)]
    for i in range(n):
        start_text, goal_text = input().split()
        start = change_time_to_sec(start_text)
        goal = change_time_to_sec(goal_text)
        div_train_num[start] += 1
        div_train_num[goal] -= 1
    train_num = 0
    train_num_max = 0
    for div in div_train_num:
        train_num += div
        if train_num_max < train_num:
            train_num_max = train_num
    print(train_num_max)


while True:
    main()
