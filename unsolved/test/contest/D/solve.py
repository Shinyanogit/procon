# -*- coding: utf-8 -*-
#しね(直球)
#https://atcoder.jp/contests/abc261/tasks/abc261_d
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
#深さ優先探索がおそらく有効、、？
#わかんないけど2bit探索してみる。計算がキツかったら後で考える
#まてまてどう考えてもおかしいN=5000だぞ
#あ動的計画法か
xlist=list(map(int,input().split()))
bonus=dict(zip(range(n+1),[0 for i in range(n+1)]))#それぞれの到達ボーナスを格納
for i in range(m):
    c,y=map(int,input().split())
    bonus[c]=y
dp=[[0]+[-100 for i in range(n)]]#ij成分はi(0-n)回目のコイントス後にカウンタがjである場合のお金の最大値。どんどん追加していく。最初はコイントス前
for i in range(1,n+1):#i(1-n)回後のコイントスの後に手に入る金額の最大値を各の場所について考える
    dp.append([-100 for i in range(n+1)])
    for j in range(1,i+1):#i回目でカウンタがj(1-i)となる場合
            dp[i][j]=dp[i-1][j-1]+xlist[i-1]+bonus[j]
    #カウンタがi回目で0となる場合
    dp[i][0]=max(dp[i-1])
# print(dp)
print(max(dp[n]))
