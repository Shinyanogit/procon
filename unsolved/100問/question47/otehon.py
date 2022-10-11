
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())
A = np.array(read().split(), np.int64)

# 順に二回並べることで円環を区間につぶしたまま作業できる
A = np.concatenate([A, A])

# dp: 残りのピースがn個（A[i:i+n]）だったとして、最終的にJOI君が得るスコア
# 小さいnから逐次的に更新していく（一次元配列を使い回す）
dp = np.zeros(N, np.int64)
for n in range(1, N + 1):#[n-1:n+N-2]を考えるっぽい
    dp = np.append(dp, dp[0])  # dpも円環
    player = (N - n) & 1  # 最後のターンから考えるので、Nが偶数なら最後はIOI、奇数なら最後はJOI
    if player == 0:
        # JOI君
        left = dp[1 : N + 1] + A[:N]
        right = dp[:N] + A[n - 1 : N + n - 1]
        dp = np.maximum(left, right)
    else:
        # IOIちゃん
        dp = np.where(A[:N] > A[n - 1 : N + n - 1], dp[1 : N + 1], dp[:N])

answer = dp.max()
print(answer)
