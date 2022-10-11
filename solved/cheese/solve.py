# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
import sys
from collections import deque
input=sys.stdin.readline
h,w,n=map(int,input().split())
input_position_map=[[alpha for alpha in list(input()) if alpha!="\n"] for line in range(h)]
position_map=[[0 for i in range(w)] for j in range(h)]
class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.condition=input_position_map[x][y]
        self.minute=-1
    def get_nears(self,position_map_with_node):
        x=self.x
        y=self.y
        xy_list=[xy for xy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=xy[0]<h and 0<=xy[1]<w]
        return [position_map_with_node[xy[0]][xy[1]] for xy in xy_list if (input_position_map[xy[0]][xy[1]]!="X")]
for x in range(h):
    for y in range(w):
        position_map[x][y]=Node(x,y)
# print(input_position_map)
for x in range(h):
    for y in range(w):
        if position_map[x][y].condition=="S":
            home=position_map[x][y]
            home.minute=0
queue=deque()
queue.append(home)
eatable_cheese=1#食べれるチーズの上限
laptime=0#最後にチーズを食べた時刻
while queue:
    node=queue.popleft()
    nears=node.get_nears(position_map)
    print(node.x,node.y,node.condition,node.minute)
    for near in nears:
        print("x,y,last visited,condition:",near.x,near.y,near.minute,near.condition)
        if laptime>near.minute:#前回のチーズから到着していない
            # print(near.x,near.y)
            if near.condition==str(eatable_cheese):#目標のチーズを食える
                if near.condition==str(n):#それが最後のチーズであった
                    print(node.minute+1)
                    exit(0)
                eatable_cheese+=1#成長
                laptime=node.minute+1#最後にチーズを食べた時刻を更新
                print(laptime)
                near.minute=node.minute+1#到達時刻の記録
                queue.clear()#探索候補をリセット
                queue.append(near)
            else:#食えるチーズがなく、未踏
                near.minute=node.minute+1
                queue.append(near)