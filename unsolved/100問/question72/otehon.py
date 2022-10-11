MOD = 10**9 + 7
W, H = map(int, input().split())
W -= 1  # コードを見やすくする
H -= 1  # コードを見やすくする
mx = 2 * 10**5
fact = [1] * (mx + 1)  # 階乗を格納するリスト


def inv(n):  # MODを法とした逆元
    return pow(n, MOD - 2, MOD)


for i in range(mx):
    fact[i + 1] = fact[i] * (i + 1) % MOD  # 階乗を計算
ans = (fact[W + H] * inv(fact[W]) * inv(fact[H])) % MOD  # comb(W+H,W) = (W+H)!/(W!H!)
print(ans)
