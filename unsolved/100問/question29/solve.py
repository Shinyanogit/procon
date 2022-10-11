# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc007/tasks/abc007_3
# 今回は1スタートで行く
# めちゃくちゃバグが多かった。実装力が付きそう
import sys, heapq



input = sys.stdin.readline
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
# sx,sy,gx,gy=sx-1,sy-1,gx-1,gy-1
distance_list = [[-1] * (w + 2) for i in range(h + 2)]  # ij成分は(j,i)にたどり着くまでの歩数
position = (
    [[False] * (w + 2)]
    + [[False] + list(input())[:-1] + [False] for i in range(h)]
    + [[False] * (w + 2)]
)  # ij成分はその座標に進めるか否か
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if position[i][j] == ".":
            position[i][j] = True
        else:
            position[i][j] = False
search_hq = [(0, sy, sx)]  # (step,y,x)
distance_list[sy][sx] = 0
heapq.heapify(search_hq)
Flag = False
while search_hq:
    if Flag:
        break
    step, y, x = heapq.heappop(search_hq)
    for x_new, y_new in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if position[y_new][x_new] and (distance_list[y_new][x_new] < 0):  # 壁がなく、未踏
            heapq.heappush(search_hq, (step + 1, y_new, x_new))
            distance_list[y_new][x_new] = step + 1
            if (x_new, y_new) == (gx, gy):
                Flag = True

print(distance_list[gy][gx])
