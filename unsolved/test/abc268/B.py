# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
flag = True
flag2 = True
a = 1
b = 10
for i in range(10):
    if flag:  # まだ見つかってない
        string = input()[:-1]
        if "#" in string:  # 探索開始
            flag = False
            temp = []
            for j in range(10):
                a = i + 1
                # print(string)
                # print(string[j])
                if string[j] == "#" and flag2:
                    # print(temp)
                    temp.append(j + 1)
            c = min(temp)
            d = max(temp)
            flag2 = False
    else:  # もう見つかった
        string = input()[:-1]
        if "#" not in string:
            b = i
            print(f"{a} {b}")
            print(f"{c} {d}")
            exit()
print(f"{a} {b}")
print(f"{c} {d}")
