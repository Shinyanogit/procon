fact = [1]
MOD = 10**9 + 7
prev_num = 1
step = 100
for i in range(step):
    fact.append((prev_num * (i + 1)) % MOD)
    prev_num = (prev_num * (i + 1)) % MOD
    if i < 100:
        print(fact[i], (i + 1), fact[i + 1])
