# -*- coding: utf-8 -*-
##https://atcoder.jp/contests/abc012/tasks/abc012_4
import sys,heapq
input=sys.stdin.readline
n,m=map(int,input().split())
paths=[[] for i in range(n)]#各バス停からの(時間,到着場所)を記録
for i in range(m):
    a,b,t=map(int,input().split())
    a,b=a-1,b-1
    paths[a].append((t,b))
    paths[b].append((t,a))
def dikstra(start):#スタート地点から各バス停までの最短経路を順々に考えてその最大値を返す関数
    cost=[float("inf")]*n#各地点までの最短経路
    hq=[(0,start)]#足を伸ばす元となる場所とその最短経路
    heapq.heapify(hq)
    cost[start]=0
    while hq:
        c,v=heapq.heappop(hq)
        if c>cost[v]:#価値なし(足を伸ばす元でない)
            continue
        #ここから足を伸ばしていく
        for t,u in paths[v]:
            tmp=cost[v]+t
            if tmp<cost[u]:#候補が最短かも、、？
                cost[u]=tmp
                heapq.heappush(hq,(tmp,u))
    return max(cost)
ans=min([dikstra(i) for i in range(n)])
print(ans)
