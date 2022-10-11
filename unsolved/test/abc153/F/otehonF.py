class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


from bisect import bisect_right as bs

N, D, A = map(int, input().split())
monsters = [list(map(int, input().split())) for _ in range(N)]
monsters.sort()
X = [monsters[i][0] for i in range(N)]
H = [(monsters[i][1] + A - 1) // A for i in range(N)]
bit = Bit(N + 5)
ans = 0
for i in range(N):
    cnt = max(0, H[i] - bit.sum(i + 1))
    ans += cnt
    idx = bs(X, X[i] + 2 * D)
    bit.add(i + 1, cnt)
    bit.add(idx + 1, -cnt)
    # print(cnt,idx)
print(ans)
