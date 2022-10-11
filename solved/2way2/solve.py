# -*- coding: utf-8 -*-
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
import sys
input=sys.stdin.readline
#n 個の整数を含む数列 S と、q 個の異なる整数を含む数列 T を読み込み、T に含まれる整数の中で S に含まれるものの個数 C を出力するプログラムを作成してください。
n=int(input())
s_list=list(map(int,input().split()))
q=int(input())
t_list=sorted(list(map(int,input().split())))
counter=0
# print(t_list)
for t_num in t_list:
    #t_numに一致する数字をs_listから探す
    left=0
    right=n-1
    mid=(n-1)//2
    post_3=[]
    # print("start",post_3,t_num)
    while True:
        if [left,mid,right]==post_3 or left==right:#前回と同じになったかあるいは狭くなりすぎた
            if s_list[left]==t_num:
                counter+=1
                break
            else:
                break
        # else:
        #     print(post_3,[left,mid,right])
        if s_list[mid]>=t_num:#rightはs_num以上
            post_3=[left,mid,right]
            right=mid
            mid=(left+right)//2
        else:
            post_3=[left,mid,right]
            left=mid+1#leftはs_num未満、、？
            mid=(left+right)//2
print(counter)