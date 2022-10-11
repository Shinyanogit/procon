# 縦横への効きを考慮すると探索範囲を減らせる。
# 今回ちょうど8つクイーンを配置するので各行に一つずつ別の列のクイーンが存在するはず。
# つまり0-7を並び替える7!で十分
# あとは8!通りについて8つのクイーンを順に置いていくので、0(nxn!)
# 深さ有線探索が使えそうではある(やらなかった)
# 斜めの効きを考えるので回転が有効
# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja
import sys, itertools

input = sys.stdin.readline
k = int(input())
rc = []
for i in range(k):
    r, c = map(int, input().split())
    rc.append((r, c))


def check(queens):
    distance_list = []
    for i in range(8):
        distance = i + queens[i]
        if distance not in distance_list:
            distance_list.append(distance)
        else:
            return False
    return True


def rotate(queens):
    rotated = [0 for i in range(8)]
    for x in range(8):
        y = queens[x]
        rotated[7 - y] = x
    return rotated


def show(queens):
    for queen in queens:
        text = ""
        for i in range(queen):
            text += "."
        text += "Q"
        for i in range(7 - queen):
            text += "."
        print(text)


queens_comb = itertools.permutations(range(8), 8)  # 順番を考える非復元抽出
for queens in queens_comb:
    flag = True
    # こっから入力に合致するものを抽出
    for r, c in rc:
        if queens[r] != c:
            flag = False
            break
    if not flag:
        continue
    # こっから斜めの効きを検討する
    # つまり4頂点からの距離がおのおの違うかどうかを検討したい
    # 原点からのチェックは16行目から
    for i in range(4):
        if check(queens):
            queens = rotate(queens)
        else:
            flag = False
            break
    if flag:
        show(queens)
        break
