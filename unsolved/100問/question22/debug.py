# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/arc054/tasks/arc054_b
# これ二分探索だ
import sys, math
import numpy as np
import matplotlib.pyplot as plt


class graph:
    def __init__(self, left, right):
        self.left = [left]
        self.right = [right]
        self.x = np.linspace(0, right, int(100 * right))
        self.y = self.x + (right**2) * np.power(2, -2 * self.x / 3)
        plt.plot(self.x, self.y)

    def save(self, left, right):
        self.left.append(left)
        self.right.append(right)

    def show(self):
        plt.plot(self.left, [calc_time(i) for i in self.left])
        plt.plot(self.right, [calc_time(i) for i in self.right])
        plt.show()


input = sys.stdin.readline
for i in range(3):
    plt.subplot(1, 3, i + 1)
    p = float(input())
    calc_time = lambda t: t + p * math.pow(2, -2 * t / 3)
    # dt = p / math.pow(10, 13)
    dt = p / (10**11)
    div_calc_time = lambda t: (calc_time(t + dt) - calc_time(t - dt)) / (2 * dt)
    left = 0
    right = math.sqrt(p)
    new_graph = graph(left, right)
    mid = (left + right) / 2
    while right - left > dt:
        if div_calc_time(mid) < 0:
            left = mid
            mid = (right + left) / 2
            new_graph.save(left, right)
        else:
            mid = (right + left) / 2
            right = mid
            new_graph.save(left, right)
    print(calc_time(mid))
    new_graph.show()

print(calc_time(90))
