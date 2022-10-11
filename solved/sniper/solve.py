# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc023/tasks/abc023_d
# 高橋君は最近、射撃にハマっている。

# 高橋君は N 個の風船すべてを射撃で割り、得られる得点をできるだけ小さくする競技に参加している。

# 風船には 1 から N までの番号が付けられていて、風船 i(1≦i≦N) は競技開始時に高度 H 
# i
# ​
#   のところにあり、1 秒経過するにつれて高度が S 
# i
# ​
#   だけ増加する。

# 高橋君は競技開始時に 1 個風船を割ることができ、そこから 1 秒ごとに 1 個の風船を割ることができる。どの順番で風船を割るのかは高橋君が自由に決定できる。

# どの風船についても、その風船を割ることによるペナルティが発生する。ペナルティはその風船が割られたときの高度と等しい整数値となる。高橋君が最終的に得る得点は N 個の風船のペナルティのうちの最大値となる。

# 高橋君が得ることのできる得点として考えられる最小値を求めよ。
import sys
import time
input=sys.stdin.readline
n=int(input())
h_list=[]
s_list=[]
for i in range(n):
    h,s=map(int,input().split())
    h_list.append(h)
    s_list.append(s)
def ok(h_max):#高さh以下をキープして全ての風船を割れるか
    time_limit_list=[]#何秒以内に打たないとダメか
    for h,s in zip(h_list,s_list):
        time_limit=(h_max-h)//s
        time_limit_list.append(time_limit)
    time_limit_list.sort()
    for i in range(n):#i番目に小さいtime_limitがi秒以上猶予があるか
        if time_limit_list[i]>=i:
            continue
        else:
            return False
    return True
#あとは大丈夫な高さを二分探索で見定める。
left=-1
right=max(h_list)+(n-1)*max(s_list)
while right-left>1:
    mid=(right+left)//2
    if ok(mid):#rightは常に大丈夫
        right=mid
    else:#leftはだいじょばない
        left=mid
print(right)