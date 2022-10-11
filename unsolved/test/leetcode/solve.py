# -*- coding: utf-8 -*-
# https://leetcode.com/contest/weekly-contest-308/problems/longest-subsequence-with-limited-sum/
import sys

input = sys.stdin.readline
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))
sorted_nums = sorted(nums)
S_nums = [0]  # i成分小さい順にnumsからi個数字を取って計算された和
current_sum = 0
for num in sorted_nums:
    current_sum += num
    S_nums.append(current_sum)
print(S_nums)


def find_max_subsequence_size(query):
    print()
    left_list = [0]  # S_nums[left]は常にquery以下
    right_list = [len(nums)]  # より大きい
    mid_list = [(len(nums)) // 2]
    right = right_list[-1]
    left = left_list[-1]
    mid = mid_list[-1]
    while right - left > 2:
        print(left, mid, right)
        right = right_list[-1]
        left = left_list[-1]
        mid = mid_list[-1]
        # print(S_nums[left], S_nums[mid], S_nums[right])
        if S_nums[mid] > query:
            right_list.append(mid)
            mid_list.append((left + mid) // 2)
            print(left, mid, right, 28)
        else:
            left_list.append(mid)
            mid_list.append((right + mid) // 2)
            print(left, mid, right, 32)
    return left


output = []
for query in queries:
    output.append(find_max_subsequence_size(query))
print(output)
