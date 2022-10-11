# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
columns = [0 for i in range(7)]
pins = input()[:-1]
for i in range(1, 11):
    id = 6
    if i == 7:
        id = 0
    elif i == 4:
        id = 1
    elif i == 2 or i == 8:
        id = 2
    elif i == 1 or i == 5:
        id = 3
    elif i == 3 or i == 9:
        id = 4
    elif id == 6:
        id = 5
    columns[id] += int(pins[i - 1])
for i in range(5):
    if columns[i] and sum(columns[i + 2 :]) and columns[i + 1] == 0 and pins[0] == "0":
        print("Yes")
        exit()
print("No")
