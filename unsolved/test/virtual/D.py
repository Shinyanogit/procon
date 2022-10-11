# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc268/tasks/abc268_d
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
s_list = [input()[:-1] for i in range(n)]
t_list = [input()[:-1] for i in range(n)]
s_list = sorted(s_list, key=len)
# for t in t_list:
#     segments = t.split("_")
#     counter = 0
#     t_counter = 0
#     _counter = 0
#     answer_seg = []
#     answer_sep = []
#     for chra in t:
#         if chra == "_":
#             t_counter = 0
#             _counter += 1
#             answer_seg.append(s_list.index(segments[counter]))
#             counter += 1
#         else:
#             t_counter += 1
#             _counter = 0

# 要するにどの文字列をどの間隔でおいているかが大事
def get_username(size):  # size個のsを並び替えて作れるusernameと_の区間を作って返却
    for comb in combinations(s_list, size):
        comb_size = 0
        for s in comb:
            comb_size += len(s)
        remaining_size = 16 - comb_size
        if remaining_size <= 0:
            continue
        for add_more in range(max(0,3-comb_size),remaining_size+1):
