# -*- coding: utf-8 -*-
# 削除するかどうかの2**20程度なら回せる
def same(columns, indexes):
    column_B, index_B = 0, 0
    for c in columns:
        for i in indexes:
            if A[c][i] != B[column_B][index_B]:
                return False
            index_B += 1
            index_B %= W2
        column_B += 1
        column_B %= H2
    return True


from itertools import combinations
import sys

input = sys.stdin.readline
H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for i in range(H1)]
# AからH1個,列をW1個選んで、比較
for columns in combinations(range(H1), H2):
    for indexes in combinations(range(W1), W2):
        if same(columns, indexes):
            # print(columns, indexes)
            print("Yes")
            exit()
print("No")
