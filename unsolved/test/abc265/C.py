# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
h, w = map(int, input().split())
directions = [list(input())[:-1] for i in range(h)]
x = 0
y = 0

# print(directions)


def next_position(x, y):
    global directions
    # print(directions)
    dx, dy = (0, 0)
    # print(x, y)
    if directions[x][y] == "U":
        dx = -1
    elif directions[x][y] == "D":
        dx += 1
    elif directions[x][y] == "L":
        dy -= 1
    elif directions[x][y] == "R":
        dy += 1
    elif directions[x][y] == "reached":
        print(-1)
        exit()
    # print("dxdy", dx, dy)
    return (x + dx, y + dy)


while True:  # x,yから移動を繰り返す
    # print(x, y)
    nx, ny = next_position(x, y)
    if nx < 0 or nx >= h or ny < 0 or ny >= w:  # ゴール
        print(f"{x + 1} {y + 1}")
        # print("1 3")
        exit()
    directions[x][y] = "reached"
    x, y = (nx, ny)
