# -*- coding: utf-8 -*-
import sys,itertools,math
input=sys.stdin.readline
number_of_city=int(input())
coordinate_list=[]
distance_list=[]
for i in range(number_of_city):
    coordinate_list.append(list(map(int,input().split())))
for order_to_visit in itertools.permutations(range(number_of_city)):#order_to_visitに従い順番に街を訪れていく
    sum_of_distance=0#距離の初期化
    current_position=coordinate_list[order_to_visit[0]]#初期位置に移動
    for next_coordinate in order_to_visit[1:]:#次の位置まで移動
        [x_new,y_new]=coordinate_list[next_coordinate]
        [x,y]=current_position
        sum_of_distance+=math.sqrt((x_new-x)**2+(y_new-y)**2)#距離の加算
        current_position=coordinate_list[next_coordinate]#位置の更新
    distance_list.append(sum_of_distance)
print(sum(distance_list)/len(distance_list))