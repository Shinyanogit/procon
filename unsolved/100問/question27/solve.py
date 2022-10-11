# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
import sys

input = sys.stdin.readline


def show(a):
    for line in a:
        print(line)
    print()


# まず周囲を0で囲う
# そのあと深さ優先探索していく
m = int(input())
n = int(input())
raw_ice_condition = [[0 for i in range(m + 2)]]
for i in range(n):
    ice = [0] + list(map(int, input().split())) + [0]
    raw_ice_condition.append(ice)
raw_ice_condition.append([0 for i in range(m + 2)])


def copy2d(twod_list):
    save_data = [[0 for i in range(m + 2)] for j in range(n + 2)]
    for i in range(n + 2):
        for j in range(m + 2):
            if twod_list[i][j]:
                save_data[i][j] = 1
    return save_data


save_data = copy2d(raw_ice_condition)


raw_ice_conditions = [raw_ice_condition for i in range(m * n)]
# for c in raw_ice_conditions:
#     show(c)


def around(ice_condition, x, y):  # まわりで進める場所を列挙
    if x == 0 or x == n + 1 or y == 0 or y == m + 1:
        return []
    result = []
    for X, Y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if ice_condition[X][Y]:
            result.append((X, Y))
    return result


def dfs(
    ice_condition, x, y, steps
):  # ice_conditionの条件下で(x,y)からスタートして深さ優先探索によってその地点から移動できる区画数の最大値を返す
    bucket = []  # そのスタート地点から進める歩数を格納
    if len(around(ice_condition, x, y)) == 0:  # もうどこにもいけない
        bucket.append(steps)
    next_step = steps + 1
    ice_condition[x][y] = 0  # 潰す
    for X, Y in around(ice_condition, x, y):
        bucket.append(dfs(ice_condition.copy(), X, Y, next_step))
    return max(bucket)


# show(raw_ice_condition)
max_move = 0
counter = 0
for x in range(1, n + 2):
    for y in range(1, m + 2):
        if save_data[x][y]:
            ice_condition = copy2d(raw_ice_condition)
            show(ice_condition)
            counter += 1
            max_move = max(max_move, dfs(ice_condition, x, y, 1))
print(max_move)
# show(raw_ice_condition)
