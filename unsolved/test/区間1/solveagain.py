# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
while True:
    n = int(input())
    if n == 0:
        break
    wlist = list(map(int, input().split()))
    dp = [[-1] * (n + 1) for i in range(n)]  # 保存用

    def clash(i, j):  # ij成分は区間[i,j)で取り除けるブロックの最大数を求める
        if j - i < 2:  # 単体、またはブロックを含まない
            ans = 0
        elif j - i == 2:  # 隣接
            if -2 < wlist[j] - wlist[i] < 2:
                ans = 2
            else:
                ans = 0
        else:
            if dp[i][j] >= 0:  # すでに探索済み
                ans = dp[i][j]
            else:  # まだ
                if (
                    -2 < wlist[i] - wlist[j - 1] < 2
                    and clash(i + 1, j - 1) == j - i - 2
                ):  # 両端が消え,かつ挟まれている部分も消える
                    ans = j - i
                else:  # 両端はペアにならない
                    ans = max([clash(i, mid) + clash(mid, j) for mid in range(i, j)])
        dp[i][j] = ans
        return ans

    clash(0, n)
    print(dp[0][n])
