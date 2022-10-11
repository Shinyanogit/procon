# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc261/tasks/abc261_d
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
alist=list(map(int,input().split()))
dp=[[False for j in range(m+1)] for i in range(n)]#ij成分はA0-Ai(iは0-n-1)までをうまく選らんで和をj(0-M)とできるか
#まずA0だけを考える
for j in range(0,m+1):
    if alist[0]==j or j==0:
        dp[0][j]=True
#A1-An-1を考える
if n>=2:
    for i in range(1,n):
        for j in range(0,m+1):
            if dp[i-1][j-alist[i]] or dp[i-1][j]:
                dp[i][j]=True
if dp[n-1][m]:
    print("Yes")
else:
    print("No")
