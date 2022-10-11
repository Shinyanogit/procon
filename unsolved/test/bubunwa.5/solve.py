# -*- coding: utf-8 -*-
# https://algo-method.com/tasks/316
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
C=[list(map(int,input().split())) for i in range(n)]
dp=[[0 for j in range(m)] for i in range(n)]#ij成分はa0-aiとb0-bjの部分一致数の最小コスト
#まず先頭(0番目)だけを考える
for j in range(0,m):#a0とb0-bjの最小コスト
    dp[0][j]=sum(C[0][0:j+1])
    # print(sum(C[0][0:j+1]))
# 徐々にaを増やしていくことを考える
for i in range(1,n):#a0-aiまでについて
    #b0について
    dp[i][0]=sum([C[j][0] for j in range(i+1)])
    for j in range(1,m):#b0-bjまでについて
        dp[i][j]=min([dp[i-1][j-1],dp[i][j-1],dp[i-1][j]])+C[i][j]#ai,bjが新たに増えた
print(dp[-1][-1])
# print(C)
# print(dp)
# print(n,m)

