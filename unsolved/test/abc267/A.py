# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
s = input()[:-1]
num = day.index(s)
print(5 - num)
