# -*- coding: utf-8 -*-
#https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b
#普通にやると計算量はO(n*2**n)
#まず適当にスタートを決めることで一列にして、それにdpを適応すればO(n²)でたえ、、、ない！n<10**9とりあえず実装はしてみる
import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N=int(readline())
A = np.array(read().split(), np.int64)
A=np.concatenate([A,A])

dp=np.zeros(N,np.int64)#区間[i,j)を考えた時の大きさの最大値
