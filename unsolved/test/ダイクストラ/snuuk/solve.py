# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d
import sys,heapq,operator
input=sys.stdin.readline
n,m,s,t=map(int,input().split())
yen_paths=[[] for i in range(n)]#i成分はi番目の街から到達できる街とそのスヌーク
snuuk_paths=[[] for i in range(n)]#i成分はi番目の街から到達できる街とそのスヌーク
for i in range(m):
    u,v,a,b=map(int,input().split())
    u,v=u-1,v-1
    yen_paths[u].append((v,a))
    snuuk_paths[u].append((v,b))
    yen_paths[v].append((u,a))
    snuuk_paths[v].append((u,b))
def dikstra(start,currency):#スタートから各地点までの特定の通貨における最安値を算出
    cost=[float("inf") for i in range(n)]
    cost[start]=0
    search_hq=[(start,0)]
    heapq.heapify(search_hq)
    if currency:#yenの場合
        while search_hq:
            v,c=heapq.heappop(search_hq)
            if c>cost[v]:
                continue
            for u,t in yen_paths[v]:
                tmp=cost[v]+t
                if tmp<cost[u]:
                    cost[u]=tmp
                    heapq.heappush(search_hq,(u,tmp))
    else:
        while search_hq:
            v,c=heapq.heappop(search_hq)
            if c>cost[v]:
                continue
            for u,t in snuuk_paths[v]:
                tmp=cost[v]+t
                if tmp<cost[u]:
                    cost[u]=tmp
                    heapq.heappush(search_hq,(u,tmp))
    return cost
yencost=dikstra(s,1)#スタートからの円
snuukcost=dikstra(t,0)#ゴールからのスヌーク
#両替をj番目にたどり着いた街で行う場合の必要コストを考える
#dikstra(s)の帰り値を小さい順にインデックスを取り順路を獲得する
jyunro=[i for i,val in sorted(enumerate(yencost),key=operator.itemgetter(1))]
mincost=float("inf")
for i in range(n):#i番目に訪れる街で両替する料金を計算する
    city=jyunro[i]#両替する街
    if city<=i:#cityで両替できない
        continue
    yen=yencost[i]#cityまでのコスト
    snuuk=snuukcost[n-1-i]#city以降のコスト
    mincost=min(yen+snuuk,mincost)
print(10**15-mincost)
