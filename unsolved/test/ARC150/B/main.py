# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
T = int(input())
def get_min_xy(A,B):
    #a+b+x+yが一定、、？
    #b+x+y/aとb/a+x+yの間に整数が挟まれるようなx+yが欲しい
    #a+b+x+yのうち２以上最小の約数で割りきった値がa+xになるんだろうね
    #和を二分探索していくのかな
    left=0
    ok=
for i in range(T):
    A, B = map(int, input().split())
    print(get_min_xy(A, B))
