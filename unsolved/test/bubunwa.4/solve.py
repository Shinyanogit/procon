# -*- coding: utf-8 -*-
# https://algo-method.com/tasks/314
import sys
input=sys.stdin.readline
s=input()[:-1]
S=len(s)
t=input()[:-1]
T=len(t)
t0=t[0]
print(s,S,t,T)
dp=[[0 for j in range(T)] for i in range(S)]#ij成分はs0-siとt0-tjの部分一致数の最大値
#まず先頭(0番目)だけを考える
for j in range(0,T):
    s0=s[0]
    if s0 in t[0:j+1]:
        dp[0][j]=1
# 徐々にsを増やしていくことを考える
for i in range(1,S):#s0-siまでについて
    #t0について
    if t0 in s[0:i+1]:
        dp[i][0]=1
    for j in range(1,T):#t1-tjまでについて
        if t[j]==s[i]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max([dp[i-1][j],dp[i][j-1]])
print(dp[-1][-1])
print(dp)
