# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# どうせ深さ優先探索やろ、、
# なんか26行目追加したらうまく行った（よくわかってない
while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    walkable = [
        list(map(int, input().split())) for i in range(h)
    ]  # ij成分は(i,j)が踏破可能か(i:0-h-1,j:0-w-1)
    island_num = 0

    def search(i, j):  # 座標(i,j)から捜索を継続
        if 0 <= i < h and 0 <= j < w and walkable[i][j]:
            walkable[i][j] = 0
            for di in range(3):
                for dj in range(3):
                    search(i + di - 1, j + dj - 1)

    def start_search(i, j):  # 座標(i,j)から新たな島の中を探索
        global island_num
        island_num += 1
        walkable[i][j] = 0
        for di in range(3):
            for dj in range(3):
                search(i + di - 1, j + dj - 1)

    for i in range(h):
        for j in range(w):
            if walkable[i][j]:
                start_search(i, j)
    print(island_num)
