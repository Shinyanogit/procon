import time

s = time.time()
import sys

sys.setrecursionlimit(10**9)
INF = 10**14
n = int(input())
di = [[-INF] * (2 * n) for _ in range(2 * n)]
a = [int(input()) for _ in range(n)] * 2


def dp(l, r):
    if l > r:
        return 0
    if di[l][r] != -INF:
        return di[l][r]
    if (n - l - r) % 2 == 0:
        if a[l] > a[r]:
            ans = dp(l + 1, r)
            di[l][r] = ans
            return ans
        else:
            ans = dp(l, r - 1)
            di[l][r] = ans
            return ans
    else:
        ans = max(dp(l + 1, r) + a[l], dp(l, r - 1) + a[r])
        di[l][r] = ans
        return ans


ans = 0
for l in range(n):
    tmp = dp(l, l + n - 1)
    if ans < tmp:
        ans = tmp
print(ans)
print(time.time() - s)
