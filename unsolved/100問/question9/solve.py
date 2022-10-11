# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
import sys

input = sys.stdin.readline
m = int(input())
find = []
for i in range(m):
    x, y = map(int, input().split())
    find.append((x, y))
n = int(input())
stars = []
for i in range(n):
    x, y = map(int, input().split())
    stars.append((x, y))


def check(a, b):  # 地図をx,y成分にa,bずらした時正座に重なるかを検証
    global find, stars
    for star_f in find:
        x, y = star_f
        x += a
        y += b
        if (x, y) in stars:
            continue
        else:
            return False
    return True


starx0, stary0 = find[0]  # 地図の0つ目の星
# これをstarsに片っ端から重ねていく
for star in stars:
    X, Y = star
    if check(X - starx0, Y - stary0):
        print(X - starx0, Y - stary0)
        break
