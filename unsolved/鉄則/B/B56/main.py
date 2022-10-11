# -*- coding: utf-8 -*-
# 文字列比較はハッシュ値でO(Q)→O(1)
# ハッシュは累乗を多用するのであらかじめ計算しておく
# O(NxQ)はまずい
# import sys

# B = 100
# MOD = 10**9 + 7

# input = sys.stdin.readline
# N, Q = map(int, input().split())
# S = input()[:-1]
# size = len(S)

# B_powered = [1]
# for i in range(size):
#     B_powered.append(B_powered[-1] * B % MOD)

# H_left = [0]
# for i in range(size):
#     H_left.append((H_left[-1] * B + ord(S[i]) - 97) % MOD)


# def hash_from_left(i, j):
#     return (H_left[j] - H_left[i - 1] * B_powered[j - i + 1]) % MOD


# H_right = [0]
# for i in range(size):
#     H_right.append((H_right[-1] * B + ord(S[i]) - 97) % MOD)


# def hash_from_right(i, j):
#     I = size + 1 - i
#     J = size + 1 - j
#     return (H_right[I] - H_right[J - 1] * B_powered[J - I - 1]) % MOD


# def kaibun(l, r):
#     return hash_from_left(l, r) == hash_from_right(l, r)


# for q in range(Q):
#     l, r = map(int, input().split())
#     print(l, r, hash_from_left(l, r), hash_from_right(l, r))
#     if kaibun(l, r):
#         print("Yes")
#     else:
#         print("No")
# print(H_right)
# print(H_left)
# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
MOD = 10**9 + 7
N, Q = map(int, input().split())
S = input()[:-1]
B = 100
B_power = [1]
for i in range(N):
    B_power.append(B_power[-1] * B % MOD)
H_left = [0]
for i in range(N):
    H_left.append((H_left[-1] * B + ord(S[i]) - 97) % MOD)
H_right = [0]
for i in range(N):
    H_right.append((H_right[-1] * B + ord(S[N - 1 - i]) - 97) % MOD)


def getHashLeft(i, j):
    return (H_left[j] - H_left[i - 1] * B_power[j - i + 1]) % MOD


def getHashRight(i, j):
    l, r = N + 1 - j, N + 1 - i
    return (H_right[r] - H_right[l - 1] * B_power[r - l + 1]) % MOD


for i in range(Q):
    L, R = map(int, input().split())
    if getHashLeft(L, R) == getHashRight(L, R):
        print("Yes")
    else:
        print("No")
