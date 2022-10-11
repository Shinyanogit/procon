# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/dp/tasks/dp_a
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[float("inf") for i in range(n)]
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n):
    # dp[i]=min([dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,min(k,i))])
    # print(i,[dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,min(k,i))])
    dp[i]=min([dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,min(k+1,i+1))])
    # print(i,[dp[i-j]+abs(h[i]-h[i-j]) for j in range(1,min(k+1,i+1))])
print(dp[-1])
# print(dp)
