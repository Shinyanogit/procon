# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
n, m, t = map(int, input().split())
a = list(map(int, input().split()))
rooms = []  # i成分にはi番目の消費時間とボーナスが格納
for a_i in a:
    rooms.append((a_i, 0))
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    rooms[x] = (a[x], y)
life = t
# print(rooms)
for room in rooms:
    cost, bonus = room
    life += bonus
    # print(life)
    if life <= cost:
        print("No")
        exit()
    life -= cost
print("Yes")
