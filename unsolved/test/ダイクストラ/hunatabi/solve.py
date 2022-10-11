# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
import sys,heapq
input=sys.stdin.readline
n,k=map(int,input().split())
paths=[[] for i in range(n)]#i番目の要素は島iから到達できる島と所要時間のリスト
def dikstra(start,goal,paths):
    cost=[float("inf") for i in range(n)]#各島の運賃の最低金額(確定したら入力)
    search_hq=[(start,0)]#探索候補(とりあえず探してみろ)
    cost[start]=0
    heapq.heapify(search_hq)
    while search_hq:
        v,c=heapq.heappop(search_hq)
        if c>cost[v]:#スルー
            continue
        #最短かも、、？
        for u,t in paths[v]:
            tmp=cost[v]+t
            if tmp<cost[u]:#候補が最短
                cost[u]=tmp#更新
                heapq.heappush(search_hq,(u,tmp))#探索候補にぶち込む
    ans=cost[goal]
    if ans!=float("inf"):
        return ans
    else:
        return -1
for i in range(k):
    information=list(map(int,input().split()))
    if information[0]:#運行情報
        c,d,e=information[1:]
        c,d=c-1,d-1
        paths[c].append((d,e))
        paths[d].append((c,e))#運行情報の更新
    else:#注文
        start,goal=information[1:]
        start,goal=start-1,goal-1
        reply=dikstra(start,goal,paths)
        print(reply)
