# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
l1,r1,l2,r2=map(int,input().split())
print(max([0,min([r2,r1])-max([l1,l2])]))
