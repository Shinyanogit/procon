# -*- coding: utf-8 -*-
# 各日程で最もお得な仕事を選ぶ
# d日目までで選べる仕事を解禁日順にheapqで更新していく
# 計算量はO(Nかなぁ)
import sys
import heapq as hq

input = sys.stdin.readline
N, D = map(int, input().split())
jobs = [tuple(map(int, input().split())) for i in range(N)]
hq.heapify(jobs)
day = 1
max_salaries = [0]
max_salary = 0
hq.heapify(max_salaries)
bank = 0
while jobs:
    next_day, pay = hq.heappop(jobs)
    if next_day == day:
        hq.heappush(max_salaries, -max_salary)
    # next_day-1日目まで仕事をしてもらう
    bank += (next_day - day) * max_salary
    # next_dayに更新
    hq.heappush(max_salaries, -pay)
    max_salary = -hq.heappop(max_salaries)
    day = next_day
    # print(day, max_salary, bank)
# 最終日のケア
bank += (D - day + 1) * max_salary
print(bank)
