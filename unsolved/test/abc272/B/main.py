# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dp = [[0] * N for i in range(N)]


# def show():
# for line in dp:
# print(line)
# print()


for i in range(M):
    input_list = list(map(int, input().split()))
    for j in range(input_list[0] - 1):
        for k in range(j + 1, input_list[0]):
            x1, x2 = input_list[j + 1], input_list[k + 1]
            if dp[x1 - 1][x2 - 1] == 0:
                dp[x1 - 1][x2 - 1] = 1
    # show()
for i in range(N - 1):
    for j in range(i + 1, N):
        # print(i, j, dp[i][j])
        if dp[i][j]:
            continue
        else:
            print("No")
            exit()
print("Yes")
