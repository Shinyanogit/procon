# -*- coding: utf-8 -*-
# https://paiza.jp/challenges/569/show
import sys

input = sys.stdin.readline
h, b = map(int, input().split())
holes = []
for i in range(h):
    x, y = map(int, input().split())
    holes.append((x, y))
current_holes = holes.copy()
balls = []
for i in range(b):
    x, y = map(int, input().split())
    balls.append((x, y))
movements = input()[:-1]  # うごかしかた
# print(holes, balls, movements)
# これから穴をmovementと逆向きに動かしていく
def duplicate(rldu):  # holes,current_holesを更新
    # print(18, rldu)
    global holes, current_holes
    new_holes = holes.copy()
    new_current_holes = []
    if rldu == "R":
        for hole in current_holes:
            x, y = hole
            new_holes.append((x - 1, y))
            new_current_holes.append((x - 1, y))
    if rldu == "L":
        for hole in current_holes:
            x, y = hole
            new_holes.append((x + 1, y))
            new_current_holes.append((x + 1, y))
    if rldu == "D":
        # print(30)
        for hole in current_holes:
            # print(32, hole)
            x, y = hole
            new_holes.append((x, y + 1))
            new_current_holes.append((x, y + 1))
    if rldu == "U":
        for hole in current_holes:
            x, y = hole
            new_holes.append((x, y - 1))
            new_current_holes.append((x, y - 1))
    holes = list(set(new_holes))
    current_holes = new_current_holes.copy()
    # print(holes)


for move in movements:
    duplicate(move)
fall_counter = 0
for ball in balls:
    if ball in holes:
        # print(ball)
        fall_counter += 1
print(fall_counter)

