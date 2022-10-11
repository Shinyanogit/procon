r1, c1, r2, c2 = map(int, input().split())
p = 10**9 + 7
n = r2 + c2 + 100
fact = [1 for _ in range(n + 1)]
inv = [1 for _ in range(n + 1)]
factinv = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    fact[i] = (fact[i - 1] * i) % p
    inv[i] = (-inv[p % i] * (p // i)) % p
    factinv[i] = (factinv[i - 1] * inv[i]) % p


def nCk(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * factinv[n - k] * factinv[k]) % p


def f(r, c):
    return nCk(r + c + 2, r + 1) - 1


print((f(r2, c2) + f(r1 - 1, c1 - 1) - f(r1 - 1, c2) - f(r2, c1 - 1)) % p)
for i in range(10):
    string = []
    for j in range(10):
        string.append(f(i, j))
    print(string)
