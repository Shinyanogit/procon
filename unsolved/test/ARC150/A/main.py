# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
T = int(input())


def only_one(N, K, S):  # Sの?を全部1にして長さがKのものが一つだけあるか判定する
    result = S
    print(N, K, S)
    more_than_k_num = 0
    length = 0
    for i, s in enumerate(S):  # i番目を最後尾にしてK個ちょうど連続させることが可能か？
        # print(more_than_k_num, length)
        if s == "1" or s == "?":
            # print(15)
            length += 1
        if s == "0":
            length = 0
        if length == K:  # 長さがKに達した
            if i == N - 1:  # 最後
                more_than_k_num += 1
            elif S[i + 1] == "?" or S[i + 1] == "0":
                more_than_k_num += 1
                # print(25)
        elif length > K:  # 長すぎ
            if S[i - K] == "?" and i == N - 1:  # 最後尾かつ、ひとつ前が?
                more_than_k_num += 1
            elif S[i - K] == "?" and (S[i + 1] == "?" or S[i + 1] == "0"):
                more_than_k_num += 1
    print(more_than_k_num, length)
    if more_than_k_num == 1:
        return True
    else:
        return False


for i in range(T):
    N, K = map(int, input().split())
    S = input()[:-1]
    if only_one(N, K, S):
        print("Yes")
    else:
        print("No")
