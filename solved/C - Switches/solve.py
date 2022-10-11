# -*- coding: utf-8 -*-
import sys,copy
input=sys.stdin.readline
[n,m]=list(map(int,input().split()))
k_s_list=[]
for i in range(m):
    k_s=list(map(int,input().split()))
    k_s_list.append(k_s)
p_list=list(map(int,input().split()))
counter=0
for i in range(2**n):#二進数でiとなるボタン状態を考える
    # global counter
    ramp=copy.copy(p_list)#ランプの初期状態(0で発光)
    for j in range(n):#j番目のボタンを反映させる
        if ((i>>j) & 1):#j番目が押された時
            for ramp_num in range(len(k_s_list)):
                k_s=k_s_list[ramp_num]
                if j+1 in k_s[1:]:
                    ramp[ramp_num]=(ramp[ramp_num]+1)%2#ランプを反転
    if 1 not in ramp:
        counter+=1
print(counter)