# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
N = int(input())
classes = list(map(int, input().split()))
classes.sort()
Q = int(input())


def find_complaints(status):
    global classes
    left = 0
    right = N - 1
    mid = (left + right) // 2
    while right - left >= 2:
        # print(left, mid, right)
        if classes[mid] > status:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid
            mid = (left + right) // 2
    # print("result : ", left, right)
    return min(abs(status - classes[left]), abs(status - classes[right]))


for i in range(Q):
    status = int(input())
    print(find_complaints(status))
    # print("-----------")
