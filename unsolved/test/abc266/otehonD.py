N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 60
dp = [[-INF] * (M + 1) for _ in range(N + 1)]  # im成分はiが先頭で、mつの和をとるときの最大値
dp[0][0] = 0
for i in range(1, N + 1):
    dp[i][0] = 0
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + j * A[i - 1])
print(dp[N][M])
