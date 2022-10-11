# -*- coding: utf-8 -*-
# かなしい
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, X, Y = map(int, input().split())
X -= 1
Y -= 1
paths = [[] for i in range(N)]
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    paths[u].append(v)
    paths[v].append(u)


def dfs(passed_list):
    print(passed_list)
    if passed_list[-1] == Y:
        text = ""
        for node in passed_list:
            text += str(node + 1) + " "
        print(text[:-1])
        exit()
    passed_list.append(None)
    print(passed_list, passed_list[-2], paths[passed_list[-2]], "yabai")
    for next_node in paths[passed_list[-2]]:
        print(next_node, "nn", paths[passed_list[-2]])
        print(passed_list)
        passed_list.pop()
        passed_list.append(next_node)
        if len(passed_list) <= 2:
            print(2)
            dfs(passed_list)
        elif next_node != passed_list[-3]:
            print("elif", next_node, passed_list[-3])
            dfs(passed_list)
        else:
            print("else")
            continue


dfs([X])
