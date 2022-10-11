# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_d
#とけなかった
import sys
input=sys.stdin.readline
# n=int(input())
n=3
def print_answer(text):
    if len(text)==n:
        if "a" in text:
            print(text)
    else:
        used_alphabet=list(set(text))
        for alphabet in sorted(list(set(used_alphabet+[chr(num) for num in range(ord(max(text+"a")),123)]))):
            print_answer(text+alphabet)
print_answer("")