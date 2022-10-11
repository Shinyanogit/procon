class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.rank = [0] * n

    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])  # 経路圧縮
            return self.parents[i]

    def unite(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            if self.rank[pi] < self.rank[pj]:
                self.sizes[pj] += self.sizes[pi]
                self.parents[pi] = pj
            else:
                self.sizes[pi] += self.sizes[pj]
                self.parents[pj] = pi
                if self.rank[pi] == self.rank[pj]:
                    self.rank[pi] += 1

    def same(self, i, j):
        return self.find(i) == self.find(j)


n, q = map(int, input().split())
uf = UnionFind(n)
for q in range(q):
    cmd, i, j = map(int, input().split())
    if cmd == 0:
        uf.unite(i, j)
    else:
        print(int(uf.same(i, j)))
