# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
import math

N, K = map(int, input().split())
print(int(math.log(N, K)) + 1)
