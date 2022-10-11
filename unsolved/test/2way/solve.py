# -*- coding: utf-8 -*-
import sys,bisect
from time import time
input=sys.stdin.readline
n,k=map(int,input().split())
alist=list(map(int,input().split()))
right=alist[-1]
start=time()
if k>right:
    print(-1)
else:
    # print(bisect.bisect_right(alist,k))
    left=0
    right=n-1#leftはk未満,rightはk以上となるように左右から近づけていく
    while right-left>2:
        print(left,right)
        mid=(left+right)//2
        if alist[mid]>=k:#rightはk以上
            right=mid
        else:#leftはk未満
            left=mid+1
            if alist[left]==k:

    print(left+1)
now=time()
print(now-start)
