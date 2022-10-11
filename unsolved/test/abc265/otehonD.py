# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
S = [0]  # 0も累積和に入れておくとsum関数の場合分け不要
a0 = 0
# print(a, n, p, q, r)
for i in range(n):
    a0 += a[i]
    S.append(a0)


def sum(x, y):  # x番目からy-1番目までの和(半閉区間で考える)
    return S[y] - S[x]


def bisect_left(k, s):  # sum(k,i)<=sを満たす最大のiを2分探索で求める関数
    if sum(k, n) <= s:
        return n  # nがokなら場合分け(こうすることで配列外参照を避けている)
    ok = k  # sum(k,k)=0<=s なのでi=kは満たす
    ng = n  # 上のifを満たさないのでsum(k,n)>s、よりi=nは満たさない
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if sum(k, mid) <= s:
            ok = mid  # i=midが条件式を満たすか判定
        else:
            ng = mid
    return ok


# 2分探索パートを関数化することで、デバッグしやすくなる！
for x in range(n + 1):
    y = bisect_left(x, p)
    if sum(x, y) != p:
        continue
    z = bisect_left(y, q)
    if sum(y, z) != q:
        continue
    w = bisect_left(z, r)
    if sum(z, w) != r:
        continue
    print("Yes")
    exit()
print("No")
