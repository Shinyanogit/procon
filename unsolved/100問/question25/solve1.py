# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
# RE！！！！と思ったら7行目追加したらいけましたーー！
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def search(i, j):
    if walkable[i][j]:
        # island_num += 1
        # print("search : ", i, j)
        walkable[i][j] = False
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if 0 <= x < h and 0 <= y < w and walkable[x][y]:
                    search(x, y)


def show(some_list):
    for line in some_list:
        print(line)


while True:
    w, h = map(int, input().split())
    island_num = 0

    def start_search(i, j):
        # print("start : ", i, j)
        global island_num
        if walkable[i][j]:
            island_num += 1
            walkable[i][j] = False
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    if 0 <= x < h and 0 <= y < w and walkable[x][y]:
                        search(x, y)
        # show(walkable)

    if w == 0 and h == 0:
        break
    position = [list(map(int, input().split())) for i in range(h)]
    walkable = [[True] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if not position[i][j]:
                walkable[i][j] = False
    for i in range(h):
        for j in range(w):
            if walkable[i][j]:
                start_search(i, j)
    print(island_num)
