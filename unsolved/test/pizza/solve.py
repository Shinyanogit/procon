# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
d=int(input())
shop_number=int(input())
order_number=int(input())
d_list=[0]+[int(input()) for i in range(shop_number-1)]
k_list=[int(input()) for i in range(order_number)]
def distance(x,y):
    simple_d=abs(x-y)
    if simple_d<d//2:
        return simple_d
    else:
        return d-simple_d
