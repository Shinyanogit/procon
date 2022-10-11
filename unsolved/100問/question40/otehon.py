MOD = 10**4
N, K = map(int, input().split())
A = [0] * N
for k in range(K):
    a, b = map(int, input().split())
    A[a-1] = b
dp = [[[0]*4 for i in range(4)] for j in range(N+1)]
dp[0][0][0] = 1
for n in range(N):
    for i in range(4):
        for j in range(4):
            for k in range(1,4):
                if A[n]!=0 and A[n]!=k: # パスタが指定されているのにkが違えばスキップ
                    continue
                if k != i or i != j: # 三日連続ではない場合
                    dp[n+1][k][i] += dp[n][i][j]
                    dp[n+1][k][i] %= MOD

ans = 0
for i in range(4): # 最終日、全ての状態の分を足す
    for j in range(4):
        ans += dp[-1][i][j]
        ans %= MOD

print (ans)
