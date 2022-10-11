# -*- coding: utf-8 -*-
import sys,copy
input=sys.stdin.readline
n,m,q=map(int,input().split())
evaluation_list=[list(map(int,input().split())) for i in range(q)]
result_list=[]#結果を入力
def evaluate(a_list):#a_listからスコアを算出
    score=0
    for test in evaluation_list:
        [a,b,c,d]=test
        if a_list[b-1]-a_list[a-1]==c:
            score+=d
    return score
def dfs(a_list):#a_list状態でのスコアを求める
    if len(a_list)==n:#ゴールまで到着
        result_list.append(evaluate(a_list))#スコアの記入
    else:#まだゴールじゃない
        for potential_next_a in range(a_list[-1],m+1):#次の数列を前回より大きく取る
            dfs(a_list+[potential_next_a])
dfs([1])
print(max(result_list))