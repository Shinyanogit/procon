from collections import defaultdict

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp1 = [[defaultdict(int) for j in range(N - i)] for i in range(N)]
for i in range(N):
    for j in range(N - i):
        if i == j == 0:
            dp1[i][j][A[i][j]] = 1
        if i > 0:
            for u in dp1[i - 1][j]:
                dp1[i][j][u ^ A[i][j]] += dp1[i - 1][j][u]
        if j > 0:
            for v in dp1[i][j - 1]:
                dp1[i][j][v ^ A[i][j]] += dp1[i][j - 1][v]
# print(dp1)
dp2 = [[defaultdict(int) for j in range(N - i)] for i in range(N)]
for k in range(N):
    i = N - 1 - k
    for l in range(N - k):
        j = N - 1 - l
        if k == l == 0:
            dp2[k][l][A[i][j]] = 1
        if k > 0:
            for u in dp2[k - 1][l]:
                if i + j != N - 1:
                    dp2[k][l][u ^ A[i][j]] += dp2[k - 1][l][u]
                else:
                    dp2[k][l][u] += dp2[k - 1][l][u]
        if l > 0:
            for v in dp2[k][l - 1]:
                if i + j != N - 1:
                    dp2[k][l][v ^ A[i][j]] += dp2[k][l - 1][v]
                else:
                    dp2[k][l][v] += dp2[k][l - 1][v]
# print(dp2)
ans = 0
for i in range(N):
    for u in dp1[i][N - 1 - i]:
        if u in dp2[N - 1 - i][i]:
            ans += dp1[i][N - 1 - i][u] * dp2[N - 1 - i][i][u]
print(ans)
