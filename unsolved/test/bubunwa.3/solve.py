# -*- coding: utf-8 -*-
# https://algo-method.com/tasks/311
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
alist=list(map(int,input().split()))
dp=[[-1 for j in range(m+1)] for i in range(n)]#ij成分はA0-Ai(iは0-n-1)までをうまく選らんでk個内に和をj(0-M)とできるか、可能ならその最小手数
#まずA0だけを考える
for j in range(0,m+1):
    if alist[0]==j:
        dp[0][j]=1
    elif j==0:
        dp[0][j]=0
#A1-An-1を考える
if n>=2:
    for i in range(1,n):
        for j in range(0,m+1):
            # print(i,j)
            if j-alist[i]>=0 and 0<=dp[i-1][j-alist[i]]:#i-1の時点でj-aiに到達ルートがある
                if dp[i-1][j-alist[i]]+1<=k:#それがk個以内
                    dp[i][j]=dp[i-1][j-alist[i]]+1
                # else:
                #     print(1)
            # else:
            #     # print(2)
            if (dp[i][j]>dp[i-1][j] or dp[i][j]<=0) and dp[i-1][j]>=0:#i-1の時点でjに到達していて、さっきのルートより短いかまだ未踏
                dp[i][j]=dp[i-1][j]
            # else:
            #     print(3,dp)
if dp[n-1][m]>0:
    print("Yes")
else:
    print("No")
# counter=0
# for line in dp:
#     print(alist[counter],line)
#     counter+=1
