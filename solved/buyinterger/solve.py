# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc146/tasks/abc146_c?lang=ja
import sys
input=sys.stdin.readline
a,b,x=map(int,input().split())
left=0#買える
right=10**9#買えない
def cost(interger):
    return a*interger+b*len(str(interger))
if cost(10**9)<=x:#10**9が買える
    print(10**9)
    exit()
while right-left>1:
    mid=(left+right)//2
    if cost(mid)<=x:#midが買える
        left=mid
    else:#midが買えない
        right=mid
print(left)