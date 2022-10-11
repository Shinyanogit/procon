# -*- coding: utf-8 -*-
#多分いけてる
import sys
from collections import deque
from tkinter import N
input=sys.stdin.readline
nodes_number=int(input())
nodes_list=[None]#nodeの保存リスト(0番目は空)
class Node:
    def __init__(self,index):
        self.index=index
        self.nears=[]
        self.distance=-1
for i in range(1,nodes_number+1):#i番目のnodeの周辺ノードを記録
    node=Node(i)
    node.nears=list(map(int,input().split()[2:]))
    nodes_list.append(node)
##これからbfsをスタートしていく
queue=deque()
nodes_list[1].distance=0#スタート地点の距離のみ特別に定める
queue.append(nodes_list[1])
while queue:#距離の記録されているqueueの左端から次なる調査対象を発見し、距離を記録する
    node=queue.popleft()
    nears=node.nears
    for nearby_node_number in nears:
        nearby_node=nodes_list[nearby_node_number]
        if nearby_node.distance==-1:#未踏の場合
            nearby_node.distance=node.distance+1#距離の更新
            queue.append(nearby_node)#探査対象の最後尾への追加
for ith_node in nodes_list[1:]:
    id=ith_node.index
    d=ith_node.distance
    print(str(id)+" "+str(d))