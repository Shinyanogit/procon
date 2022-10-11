# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
MOD = 10**4
pasta_data = [(list(map(int, input().split()))) for i in range(K)]
pasta_data.sort()
dp = [
    [[0] * 4 for i in range(4)] for j in range(N + 1)
]  # iをn日目に食べjをn-1日前に食べているような、n日目までのパターン数をdp[n][i][j]として表します.なお0をダミーのパスタとします
dp[0][0][0] = 1
for n in range(1, N + 1):  # i(1-N)日目について考える
    if not pasta_data == []:
        if pasta_data[0][0] != n:  # 特に指定がない
            for i in range(4):
                for j in range(4):  # n日前にi,n-1日前にjを食べている通りを考える
                    # dp[n][i][j]を考えたい
                    sum = 0
                    for k in range(4):  # n-2日目がkであった
                        if j == k:
                            if i == j:
                                continue
                            else:
                                sum += dp[n - 1][j][k]
                        else:
                            sum += dp[n - 1][j][k]
                            print(sum)
                    dp[n][i][j] = sum
    else:  # 指定がある
        day, pasta = pasta_data[0]
        pasta_data.remove(pasta_data[0])
        for i in range(4):
            if pasta == i:
                for j in range(4):
                    sum = 0
                    for k in range(4):  # n日目にpasta=i,n-1日目にj,n-2日にkを食っていた
                        if j == k:
                            if pasta == j:  # 秋田
                                continue
                            else:
                                sum += dp[n - 1][j][k]
                        else:
                            sum += dp[n - 1][j][k]
                    dp[n][pasta][j] = sum
            else:  # 制約を守らない
                for j in range(4):
                    dp[n][i][j] = 0
print(dp)
ans = 0
for i in range(4):
    for j in range(4):
        ans += dp[N][i][j]
        ans %= MOD
print(ans)
