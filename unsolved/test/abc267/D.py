# -*- coding: utf-8 -*-
import sys
from itertools import permutations

# なんかコーナーケースで引っかかる
# O(n!*logm)もいけそうだね
input = sys.stdin.readline
n, m = map(int, input().split())
S = [input()[:-1] for i in range(n)]
T = set()
for i in range(m):
    T.add(input()[:-1])
size = 0
for s in S:
    size += len(s)
add_num = 16 - size
if add_num < 0:
    print(-1)
    exit()
if len(S) == 1:
    if S[0] in T:
        print(-1)
    else:
        print(S[0])
    exit()


def create_strings(some_list, string, remaining_num):  # リストをくっつけてTと比較するコード
    answer = string
    answer_list = some_list[1:]
    if len(some_list):  # まだくっつけないと
        if remaining_num:  # まだくっつける余裕あり
            for i in range(1, remaining_num + 1):  # i個くっつけよ
                answer = string + "_" * i + some_list[0]
                answer_num = remaining_num - i
                create_strings(answer_list, answer, answer_num)
        else:
            return 0
    else:  # もう完成らしい
        if len(string) > 2:
            if string not in T:
                print(string)
                exit()
            else:
                return 0


for comb in permutations(S, len(S)):
    # print(comb)
    create_strings(list(comb)[1:], (list(comb)[0]), add_num)
print(-1)
