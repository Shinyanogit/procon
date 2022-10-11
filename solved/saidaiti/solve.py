# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
nstr=input()
print(nstr)
print(len(nstr))
n=int(nstr)
alist=list(map(int,input().split()))
dp=[0 for i in range(n+1)]#i番目までの数字の中で適当な和を取った時の最大値
for i in range(n):#i番目のdpを元にi+1番目のdpを決定
    prev=dp[i]
    if alist[i]>0:
        dp[i+1]=prev+alist[i]
    else:
        dp[i+1]=prev
print(dp[-1])
