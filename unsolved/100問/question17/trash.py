# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja
import sys, itertools
#64C8を検討したお馬鹿さんがこちらです

input = sys.stdin.readline
k = int(input())
placable = [[1] * 8 for i in range(8)]


def change_position(r, c, placable):
    if placable[r][c]:
        tmp = [(r, c)]
        for i in range(1, 8):
            tmp.extend([(r - i, c - i), (r - i, c + i), (r + i, c - i), (r + i, c + i)])
        for rx, cy in tmp:
            if 0 <= rx < 8 and 0 <= cy < 8:
                placable[rx][cy] = 0
        return (True, placable)
    else:
        return (False, placable)


for i in range(k):
    r, c = map(int, input().split())
    result, placable = change_position(r, c, placable)
# こっからランダム
mix_position = []
for i in range(8):
    for j in range(8):
        mix_position.append((i, j))
queens_comb = itertools.combinations(mix_position, 8 - k)  # mixから8-kつランダムに非復元抽出
for queens in queens_comb:
    # print(queens)
    result = True
    placable1 = placable.copy()
    for queen in queens:
        if result:
            r, c = queen
            result, placable1 = change_position(r, c, placable1)
            if not result:
                break
        else:
            break
    if result:
        print(queens)
