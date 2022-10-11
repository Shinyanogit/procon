# -*- coding: utf-8 -*-
# 貪欲かなぁ、k回のスワップ以内で作れる
# dpなきもしてきた。あらかじめAの方をsortしておいて、Bの方を揃えにいくみたいな、、？
import sys

# from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A, B = zip(*sorted(zip(A, B)))
# k番目までの数列を対象にして長さの和が最大になるように並べ替えた時のA,Bの最長部分列を記録してみるか？
INF = 1 << 60
# A_max = A[0]
B_max = B[0]
dp = [(set(A[:1]), set(B[:1]))]  # 0番目まで
for i in range(
    1, N
):  # bisectでBを入れてあげればBの入れ替えで+2確定、Aは-1なのでトータルで+だね！微妙な時はBの部分列を充実させてあげた方が良さげ.でもBの値にかぶりがある時とかその逆なら話は別かも
    a, b = (
        A[i],
        B[i],
    )
    A_i, B_i = dp[-1]
    # print(a, b)
    # priority="B":#特になければB
    # b_index_right=bisect_right(b,B_i)
    # b_index_left=bisect_left(b,B_i)
    if A[i - 1] == a:  # B優先確定
        B_i.add(b)
        # print(33)
    elif b in B_i:  # Bの中にbがすでにあるのでAを優先したい
        A_i.add(a)
        # print(36)
    else:  # AもBも更新可能
        # # 迷ったらBでしょ（適当）
        # priority = "B"
        # B_i.add(b)
        # if B_max < b:
        #     A_i.add(a)
        # 迷ったらAかも
        A_i.add(a)
        if B_max < b:
            B_i.add(b)
        # print(41)
    B_max = max(B_max, b)
    # dp.append((A_i, B_i))
    print(A_i, B_i)
A_ans, B_ans = dp[-1]
print(len(A_ans) + len(B_ans))
