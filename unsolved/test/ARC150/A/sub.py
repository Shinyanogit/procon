# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
T = int(input())


def only_one(N, K, S):  # Sの?を全部1にして長さがKのものが一つだけあるか判定する
    one_indexes = []
    for i,s in enumerate(S):
        if s=="1":
            one_indexes.append(i)
    # mode = 0
    # question_left = 0
    # one_mid = 0
    # question_right = 0
    if len(one_indexes)==0:
        length=0
        max_length=0
        for i,s in enumerate(S):
            if s=="?":
                length+=1
            if length>max_length:
                max_length=length
        if max_length==K:
            print("Yes")
        else:
            print("No")
    if len(one_indexes)==1:
        max_left=0
        max_right=0
        for s in reversed(S[:one_indexes[0]]):
            if s=="?":
                max_left+=1
            else:
                break
        for s in S[one_indexes[0]+1:]:
            if s=="?":
                max_right+=1
            else:
                break
        if max_right+max_left-2<K-1:
            print("No")
        else:
            print("Yes")
    if len(one_indexes)>=2:
        max_left=0
        mid_length=0
        max_right=0
        for s in reversed(S[:one_indexes[0]]):
            if s=="?":
                max_left+=1
            else:
                break
        for s in S[one_indexes[-1]+1:]:
            if s=="?":
                max_right+=1
            else:
                break
        for mid in S[one_indexes[0]+1:one_indexes[-1]]:
            if mid=="0":
                print("No")
                break
            mid_length+=1
        if mid_length!=one_indexes[-1]-one_indexes[0]+1:
            print("No")
            exit()
        if max_left+mid_length+max_right-2<K

    for i, s in enumerate(S):
        # if mode == 0:
        #     if s == "?":
        #         question_left += 1
        #     elif s == "0":
        #         question_left = 0
        #     else:
        #         mode = 1
        #         one_mid += 1
        # if mode == 1:
        #     if s == "0":
        #         break
        #     elif s == "1":
        #         mode = 2
        #         one_mid += 1
        #     else:
        #         one_mid += 1
        # id mode

        # if s == "1":
        #     indexes.append(i)


for i in range(T):
    N, K = map(int, input().split())
    S = input()[:-1]
    if only_one(N, K, S):
        print("Yes")
    else:
        print("No")
