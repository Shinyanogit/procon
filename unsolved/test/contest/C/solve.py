# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
n=int(input())
dic={}
def name_with_number(name,number):
    if number>=2:
        return name+f"({number-1})"
    else:
        return name
for i in range(n):
    s=input()[:-1]
    dic.setdefault(s,0)
    dic[s]+=1
    print(name_with_number(s,dic[s]))
