# -*- coding: utf-8 -*-
#
import sys

input = sys.stdin.readline


# def area(a, b, c,d):


a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
d = tuple(map(int, input().split()))

ax, ay = a
bx, by = b
cx, cy = c
dx, dy = d
cross_a = (dx - ax) * (by - ay) - (dy - ay) * (bx - ax)
cross_b = (ax - bx) * (cy - by) - (ay - by) * (cx - bx)
cross_c = (bx - cx) * (dy - cy) - (by - cy) * (dx - cx)
cross_d = (cx - dx) * (ay - dy) - (cy - dy) * (ax - dx)
if cross_a < 0 and cross_b < 0 and cross_c < 0 and cross_d < 0:
    print("Yes")
else:
    print("No")
# このコードはなぜかダメだった
# s1 = (cy - by) * (ax - bx) - (ay - by) * (cx - bx) / 2#対角線がAC
# s2 = (cy - dy) * (ax - dx) - (ay - dy) * (cx - dx) / 2#対角線がAC
# s3 = (by - ay) * (dx - ax) - (dy - ay) * (bx - ax) / 2#対角線がBD
# s4 = (by - cy) * (dx - cx) - (dy - cy) * (bx - cx) / 2#対角線がBD
# if s1 * s2 < 0 and s3 * s4 < 0:
#     print("Yes")
# else:
#     print("No")
