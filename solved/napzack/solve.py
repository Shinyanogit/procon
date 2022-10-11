# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
N,W=map(int,input().split())
dp=[[0 for j in range(W+1)] for i in range(N+1)]#[i（0-N）番目までの数字を用いて重さj(0-W)以内における価値の最大値]
for i in range(1,N+1):#i番目の最大値を考える
    w,v=map(int,input().split())#i番目の品物の入荷
    for j in range(0,W+1):#各々の重さ制限において
        if w<=j:#i番目がそもそも積める
            dp[i][j]=max([dp[i-1][j-w]+v,dp[i-1][j]])
        else:#i番目が積めない
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
