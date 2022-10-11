# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
edges = [set() for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].add(b + 1)
    edges[b].add(a + 1)
for i in range(N):
    if len(edges[i]):
        print(f"{i+1}: {edges[i]}")
    else:
        print(f"{i+1}: {{}}")
