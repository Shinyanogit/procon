# -*- coding: utf-8 -*-
import sys,itertools,copy
input=sys.stdin.readline
n,k=map(int,input().split())
height_list=[0]+list(map(int,input().split()))
##適当なkつのビルを指定して無理矢理見えるようにするためのコストを保存してから最小金額を算出する。
cost_list=[]#必要コストの保存場所
for chosen_buildings in itertools.combinations(range(n),k):
    cost=0#コストの初期化
    update_height_list=copy.copy(height_list)
    chosen_buildings_list=list(chosen_buildings)
    for building in chosen_buildings_list:#左から順にビルを高くしていく
        max_height=max(update_height_list[:building+1])#指定されたビルより左で一番高いビルの高さ
        if max_height>=update_height_list[building+1]:#それが指定されたビル以上の高さだった場合
            cost+=max_height-update_height_list[building+1]+1
            update_height_list[building+1]=max_height+1#それより１mだけ高くする
    cost_list.append(cost)
print(min(cost_list))
        