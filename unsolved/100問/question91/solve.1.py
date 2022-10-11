# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc144/tasks/abc144_d
# なんか角度が大きいとダメです
import sys, math

input = sys.stdin.readline
a, b, x = map(int, input().split())
delta = 1 / math.pow(10, 11)
left = 0
right = math.pi / 2
mid = (left + right) / 2
if x < (a**2 * b) / 2:
    # tanθ=ab²/2を解く
    k = a * (b**2) / 2
    # while right - left > delta:
    for i in range(100000):
        if math.tan(mid) < k:
            left = mid
            mid = (left + right) / 2
        else:
            right = mid
            mid = (left + right) / 2
else:
    # tanθ=2b/a-2x/a³を解く
    k = 2 * b / a - 2 * x / (a**3)
    # while right - left > delta:
    for i in range(100000):
        if math.tan(mid) < k:
            left = mid
            mid = (left + right) / 2
        else:
            right = mid
            mid = (left + right) / 2
print(180 * mid / math.pi)

# # -*- coding: utf-8 -*-
# # https://atcoder.jp/contests/abc144/tasks/abc144_d
# import sys, math

# input = sys.stdin.readline
# a, b, x = map(int, input().split())
# delta = 1 / math.pow(10, 11)
# left = 0
# right = math.pi / 2
# mid = (left + right) / 2
# if x < (a**2 * b) / 2:
#     # tanθ=ab²/2を解く
#     k = a * (b**2) / 2
#     if k < 1:  # θを考える
#         while right - left > delta:
#             if math.tan(mid) < k:
#                 left = mid
#                 mid = (left + right) / 2
#             else:
#                 right = mid
#                 mid = (left + right) / 2
#     else:  # α=pi/2-θを考える
#         while right - left > delta:
#             if math.tan(mid) < 1 / k:
#                 left = mid
#                 mid = (left + right) / 2
#             else:
#                 right = mid
#                 mid = (left + right) / 2
#         mid = math.pi / 2 - mid
# else:
#     # tanθ=2b/a-2x/a³を解く
#     k = 2 * b / a - 2 * x / (a**3)
#     if k < 1:
#         while right - left > delta:
#             if math.tan(mid) < k:
#                 left = mid
#                 mid = (left + right) / 2
#             else:
#                 right = mid
#                 mid = (left + right) / 2
#     else:
#         while right - left > delta:
#             if math.tan(mid) < 1 / k:
#                 left = mid
#                 mid = (left + right) / 2
#             else:
#                 right = mid
#                 mid = (left + right) / 2
#         mid = math.pi / 2 - mid
# print(180 * mid / math.pi)
