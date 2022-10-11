# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/abc012/tasks/abc012_4
import sys,heapq
input=sys.stdin.readline
n,m=map(int,input().split())
road_list=[[] for i in range(n)]#i成分はi番目のバス停から到着できる場所と、そこまでの距離のsetリスト
for i in range(m):
    a,b,t=map(int,input().split())
    a,b=a-1,b-1
    road_list[a].append((t,b))
    road_list[b].append((t,a))
#ここからスタート地点を全て試して最悪の経路を列挙していく
def dikstra(start):#スタートから各地点までの最短距離をダイクストラ法で求めリストで出力する
    hq=[(0,start)]#各地点とその到達時刻の候補を打刻
    heapq.heapify(hq)
    cost=[float("inf")]*n#各地点の最短到達時刻を打刻
    cost[start]=0
    while hq:
        c,v=heapq.heappop(hq)
        if c>cost[v]:#スルー
            continue
        for t,u in road_list[v]:#vからさらに到達時刻の候補を伸ばしていく
            tmp=cost[v]+t
            if tmp<cost[u]:#候補が最短となる
                cost[u]=tmp
                heapq.heappush(hq,(tmp,u))
    return cost
ans=float("inf")
for start in range(n):
    distance_list=dikstra(start)
    ans=min(ans,max(distance_list))
print(ans)
