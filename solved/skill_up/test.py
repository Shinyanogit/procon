# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
n,m,x=map(int,input().split())
cost_list=[]#i番目の教材の値段
level_up_list=[]#i番目の教材の理解度リスト
for line in range(n):
    temp_list=list(map(int,input().split()))
    cost_list.append(temp_list[0])
    level_up_list.append(temp_list[1:])
minimum_cost=sum(cost_list)+1#うまくいった場合の最小金額をここに保存
for text_book_order in range(2**n):#二進数表示におけるtextbook_orderの注文をした時
    level=[0 for i in range(m)]
    payment=0
    for j in range(n):#j番目の教材を学習させる
        if ((text_book_order>>j)&1):#購入するなら
            payment+=cost_list[j]#コストを追加
            level=[level[k]+level_up_list[j][k] for k in range(m)]#理解度を更新
    if False not in [each_level>=x for each_level in level]:#levelが全てx以上なら
        # print("payment_added",payment)
        if minimum_cost>payment:#最小なら使用料金を追加
            minimum_cost=payment
if minimum_cost<=sum(cost_list):#更新がされていれば
    print(minimum_cost)
else:
    print(-1)