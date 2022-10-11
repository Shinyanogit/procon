# -*- coding: utf-8 -*-
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
import sys
input=sys.stdin.readline
def rec(l,r,dp,w_list):#lからrで省けるブロックの最大数を返す
    if dp[l][r]!=-1:#登録済み
        return dp[l][r]
    if l==r:#区間が潰れている
        dp[l][r]=0
        return 0
    if l+1==r:#区間が隣接
        if abs(w_list[l]-w_list[r])<=1:#はじける
            dp[l][r]==2
            return 2
        else:
            dp[l][r]=0
            return 0
    #区間が3つ以上にまたがっている
    res=0
    if abs(w_list[l]-w_list[r])<=1 and rec(l+1,r-1,dp,w_list)==r-l-1:#左端と右端がペアとなり、その間も消えてくれる
        dp[l][r]=r-l+1
        return r-l+1
    else:#左端と右端はペアにならない
        for mid in range(l,r):
            res=max(res,rec(l,mid,dp,w_list)+rec(mid+1,r,dp,w_list))
        dp[l][r]=res
        return res
while True:
    n=int(input())
    if n==0:
        break
    w_list=list(map(int,input().split()))
    dp=[[-1 for i in range(n)] for j in range(n)]#ij成分は区間[i,j]で除ける最大数
    print(rec(0,n-1,dp,w_list))
    # for line in dp:
    #     print(line)
