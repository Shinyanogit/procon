# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/dp/tasks/dp_a
import sys
input=sys.stdin.readline
n=int(input())
h=list(map(int,input().split()))
dp=[float("inf") for i in range(n)]
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n):
    dp[i]=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))
print(dp[-1])
print(dp)
