# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/dp/tasks/dp_y
import sys
input=sys.stdin.readline
h,w,n=map(int,input().split())
masumap=[[1]*w for i in range(h)]#ij成分は高さi横jのマス状態
ways=[[0]*w for i in range(h)]#ij成分は（i,j）にたどり着く経路数
for i in range(n):
    r,c=map(int,input().split())
    masumap[r-1][c-1]=0
#まず一列目および１行目を埋める
for i in range(h):
    if masumap[i][0]:#壁がない
        ways[i][0]=1
    else:
        break
for j in range(w):
    if masumap[0][j]:#壁がない
        ways[0][j]=1
    else:
        break
for height in range(1,h):
    for width in range(1,w):
        if masumap[height][width]:#壁がない
            ways[height][width]=(ways[height-1][width]+ways[height][width-1])%(10**9+7)
        if (height+width)%int((h*w)**0.5)==0:
            print("going..",(height,width))
print(ways[-1][-1]%(10**9+7))
# for line in masumap:
#     print(line)
# print("----------")
# for line in ways:
#     print(line)
