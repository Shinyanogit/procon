P = 10**9 + 7
N, A, B = map(int, input().split())


def nCk(n, k):  # nが非常に大きいver
    ans = 1
    for i in range(k):
        ans *= n - i
        ans %= P
        ans *= pow(i + 1, P - 2, P)
        ans %= P
    return ans


print((pow(2, N, P) - nCk(N, A) - nCk(N, B) - 1) % P)
