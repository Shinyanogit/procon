# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline
H = int(input())


def attack_num(H):
    if H == 1:
        return 1
    if H == 0:
        return 0
    return 2 * attack_num(H // 2) + 1


print(attack_num(H))
