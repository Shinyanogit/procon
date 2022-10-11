# -*- coding: utf-8 -*-
# https://algo-method.com/tasks/311
# なんかうまくいかない
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
alist=list(map(int,input().split()))
dp=[[-1 for j in range(m+1)] for i in range(n)]#ij成分はA0-Ai(iは0-n-1)までをうまく選らんで和をj(0-M)とできるか
#まずA0だけを考える
for j in range(0,m+1):
    if alist[0]==j or j==0:
        dp[0][j]=1
#A1-An-1を考える
if n>=2:
    for i in range(1,n):
        for j in range(0,m+1):
            if j-alist[i]>=0 and 0<dp[i-1][j-alist[i]]:#i-1の時点でj-aiに到達ルートがある
                dp[i][j]=dp[i-1][j-alist[i]]+1
            if (dp[i][j]>dp[i-1][j] or dp[i][j]<0) and dp[i-1][j]>0:#i-1の時点でjに到達していて、さっきのルートより短いかまだ未踏
                dp[i][j]=dp[i-1][j]
print(dp[n-1][m])
counter=0
for line in dp:
    print(alist[counter],line)
    counter+=1
