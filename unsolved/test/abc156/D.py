# -*- coding: utf-8 -*-
# 2**n-nCa-nCbを考えればよろしい
# nCkの計算量はkまで落とせる
import sys

MOD = 10**9 + 7
input = sys.stdin.readline
n, a, b = map(int, input().split())
# INF = 1 << 60
# factorials=[1]
# inv=[1]
# factinv=[1]
# for i in  range(n):
#     factorials[i+1]=factorials[i]*(i+1)%MOD
#     inv[i+1]=-inv[MOD%i]*(MOD//i)
#     factinv[i+1]=factinv[i]*inv[i]%MOD
def nCk(n, k):  # めっちゃnが大きい時
    ans = 1
    for i in range(k):
        ans *= n - i
        ans %= MOD
        ans *= pow(i + 1, MOD - 2, MOD)
        ans %= MOD
    return ans


# tank = [INF for i in range(n + 1)]
# tank[0] = 1
# tank[1] = a


# def find_pow(a, n):
# if tank[n] != INF:
# return tank[n]
# if n % 2:
# tank[n] = (find_pow(a, n // 2) ** 2) % MOD
# return (find_pow(a, n // 2) ** 2) % MOD
# else:
# tank[n] = (a * find_pow(a, n // 2) ** 2) % MOD
# return (a * find_pow(a, n // 2) ** 2) % MOD


# print(find_pow(2, n))
# print(tank)
# print((pow(2, n, MOD) - nCk(n, a) - nCk(n, b)) % MOD)
print((pow(2, n, MOD) - nCk(n, a) - nCk(n, b) - 1) % MOD)
# print(nCk(2, 1), pow(2, 5, MOD))
