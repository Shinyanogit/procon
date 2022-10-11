# -*- coding: utf-8 -*-
#DPだよ！
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
rocks = list(map(int, input().split()))


def find_min_rock(n):  # n以下で最大の石を考える
    ok = 0
    ng = K - 1
    mid = (ok + ng) // 2
    while ng - ok > 1:
        if rocks[mid] > n:
            ng = mid
            mid = (ok + ng) // 2
        else:
            ok = mid
            mid = (ok + ng) // 2
    return rocks[ok]


def two_turns(n, takahashi):
    if n >= rocks[-1]:
        n1 = n - rocks[-1]
        takahashi += rocks[-1]
        # print(rocks[-1])
    else:
        rock_size1 = find_min_rock(n)
        n1 = n - rock_size1
        takahashi += rock_size1
        # print(rock_size1)
    if n1 == 0:
        return (0, takahashi)
    if n1 > rocks[-1]:
        # print(rock_size1)
        return (n1 - rocks[-1], takahashi)
    else:
        rock_size2 = find_min_rock(n1)
        # print(rock_size2)
        return (n1 - rock_size2, takahashi)


takahashi = 0
while N > 0:
    N, takahashi = two_turns(N, takahashi)
    # print(N)
print(takahashi)
