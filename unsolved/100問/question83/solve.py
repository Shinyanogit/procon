# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_a
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# fares=[]#i成分は区間i(駅からi+1駅を結ぶ経路)の情報(紙切符、ic代金,icカード代金)
# for i in range(n-1):
#     a,b,c=map(int,input().split())
#     fares.append((a,b,c))
# これから各区間を通る回数を計算する
# 愚直にやるとO(m*n)なので、階差数列を先に求める
path_counter = [0]  # i成分は区間i[i,i+1)(0,1,2,,,n-2)を通る回数ai
divpathcounter = [0 for i in range(n - 1)]  # pathの階差数列,i成分はai+1-ai(i=0,1,2,3,,n-3)
plist = list(map(int, input().split()))
for i in range(m - 1):
    s, g = plist[i], plist[i + 1]
    start, goal = min(s - 1, g - 1), max(s - 1, g - 1)
    if start == 0:
        path_counter[0] += 1
    else:
        divpathcounter[start - 1] += 1
    if goal < n - 1:
        divpathcounter[goal - 1] -= 1
for i in range(n - 2):
    path_counter.append(path_counter[i] + divpathcounter[i])
# こののち、各区間に対してicカードを買うか検討する(計算量0(n))
cost = 0
for i in range(n - 1):
    count = path_counter[i]
    a, b, c = map(int, input().split())
    ticket = a * count
    ic = count * b + c
    cost += min(ticket, ic)
print(cost)
