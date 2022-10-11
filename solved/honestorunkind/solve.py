# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
n=int(input())
personal_infos=[]
for person in range(n):
    assertion_list=[]
    a=int(input())
    for asserion in range(a):
        [x,y]=list(map(int,input().split()))
        assertion_list.append((x,y))
    personal_infos.append(assertion_list)
###
# print(personal_infos)
###
max=0
for i in range(2**n):#二進数でiとなる正直者状態を考える
    flag=True
    honest_or_not_list=[(i>>j&1) for j in range(n)]
    for j in range(n):
        if honest_or_not_list[j]:#j人目の人が正直者であれば
            for x,y in personal_infos[j]:#j人目の人の証言をチェック
                if honest_or_not_list[x-1]!=y:#嘘はあるかな
                    flag=False
                    break
        if not flag:
            break
    # print(honest_or_not_list)
    honest_sum=sum(honest_or_not_list)
    if honest_sum>max and flag:
        max=honest_sum
print(max)