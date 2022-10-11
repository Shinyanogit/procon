# -*- coding: utf-8 -*-
# 文字列比較はハッシュ値でO(Q)→O(1)
# ハッシュは累乗を多用するのであらかじめ計算しておく
# O(NxQ)はまずい
import sys

B = 100
MOD = 10**9 + 7

input = sys.stdin.readline
N, Q = map(int, input().split())
S = input()[:-1]
size = len(S)

B_powered = [1]
for i in range(size):
    B_powered.append(B_powered[-1] * B % MOD)

H_left = [0]
for i in range(size):
    H_left.append((H_left[-1] * B + ord(S[i]) - 97) % MOD)


def hash_from_left(i, j):
    return (H_left[j] - H_left[i - 1]) % MOD


H_right = [0]
for i in range(size):
    H_right.append((H_right[-1] * B + ord(S[size - 1 - i])) % MOD)


def hash_from_right(i, j):
    return (H_right[size + 1 - i] - H_right[size - j]) % MOD


def kaibun(l, r):
    return hash_from_left(l, r) == hash_from_right(l, r)


for q in range(Q):
    l, r = map(int, input().split())
    if kaibun(l, r):
        print("Yes")
    else:
        print("No")
