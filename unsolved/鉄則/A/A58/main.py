# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
# RMQなら更新と最大値の返却がlogNで実行可能
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
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

    # クエリ 2 に対する処理
    # u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return -1000000000  # 一切含まれない場合
        if l <= a and b <= r:
            return self.dat[u]  # 完全に含まれる場合
        m = (a + b) // 2
        answerl = self.query(l, r, a, m, u * 2)
        answerr = self.query(l, r, m, b, u * 2 + 1)
        return max(answerl, answerr)


Z = segtree(N)
for q in [tuple(map(int, input().split())) for i in range(Q)]:
    tp, *cont = q
    if tp == 1:
        pos, x = cont
        Z.update(pos - 1, x)
    if tp == 2:
        l, r = cont
        answer = Z.query(l - 1, r - 1, 0, Z.size, 1)
        print(answer)
