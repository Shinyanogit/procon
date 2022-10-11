# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/dp/tasks/dp_l
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[[0]*n for i in range(n)]#ij成分はai-ajまででゲームを進めた時のxーyの結果
for i in range(n):
    if n%2:#nが偶数ならカードが一枚の時は二郎の先攻0
        dp[i][i]=a[i]
    else:
        dp[i][i]=-a[i]
for j_minus_i in range(1,n+1):
    #j_minus_iがnの時は太郎が先攻
    if (j_minus_i-n+1-1)%2:#太郎が先攻
        for i in range(0,n-j_minus_i):
            dp[i][i+j_minus_i]=max(dp[i][i+j_minus_i-1]+a[i+j_minus_i],dp[i+1][i+j_minus_i]+a[i])
    else:#次郎が先攻
        for i in range(0,n-j_minus_i):
            dp[i][i+j_minus_i]=min(dp[i][i+j_minus_i-1]-a[i+j_minus_i],dp[i+1][i+j_minus_i]-a[i])
print(dp[0][-1])
# print(a)
# print("---------")
# for line in dp:
#     print(line)
