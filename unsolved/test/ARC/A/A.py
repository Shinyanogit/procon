# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# if M < 10:
#     # 処理
#     max1 = M * (10**N - 1) // 9
#     max2 = -1
#     num = 1
#     for n in range(N):
#         if num % M == 0:
#             max2 = 10**n - 1
#         num = num * 10 + 1
#     print(max(max1, max2))
#     exit()
# num = 1
# max1 = -1
# for n in range(N):
#     print()
#     if num % M == 0:
#         max1 = 10**n - 1
# max_num = -1
continuous1 = [0]
answer = ""
for i in range(N):
    # power10.append((power10[-1] * 10) % M)
    continuous1.append((continuous1[-1] * 10 + 1) % M)
for i in range(1, N + 1):
    for j in range(1, 10):
        # print(j * (power10[i] - 1) // 9, M)
        if (j * continuous1[i]) % M == 0:
            answer = str(j) * i
            # max_num = j * (power10[i] - 1) // 9
if len(answer) > 0:
    print(answer)
else:
    print(-1)
# print(max_num)
