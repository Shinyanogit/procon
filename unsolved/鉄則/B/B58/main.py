# -*- coding: utf-8 -*-
#
import sys
from bisect import bisect_left, bisect_right


class segtree:
    # 要素 dat の初期化を行う（最初は全部ゼロ）
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] * (self.size * 2)

    # クエリ 1 に対する処理
    def update(self, pos, x):
        pos += self.size  # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = min(self.dat[pos * 2], self.dat[pos * 2 + 1])

    # クエリ 2 に対する処理
    # u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return 1000000000  # 一切含まれない場合
        if l <= a and b <= r:
            return self.dat[u]  # 完全に含まれる場合
        m = (a + b) // 2
        answerl = self.query(l, r, a, m, u * 2)
        answerr = self.query(l, r, m, b, u * 2 + 1)
        return min(answerl, answerr)


def get_indexs(x):
    #x-R以上の要素の左端と、x-Lより大きい要素のサタンを返す


input = sys.stdin.readline
N, L, R = map(int, input().split())
# n詰めまでの足場を使ってn+1つめの足場にアプローチするときのジャンプ回数を考えたい
# 更新のために必要なのはx-r~x-lの間の最小値、、？！
# セグ木のライブラリを編集しておくことが必要
Z = segtree(N)
Z.update(0, 0)
# dp = [0]  # 足場iに辿り着くための最小ジャンプ数
for i in range(N - 1):
    l, r = get_indexs(X[i])
    next_step = Z.query(0, i + 1, left, right, 1) + 1
    Z.update(i + 1, next_step)
print(Z.dat)
