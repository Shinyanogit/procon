from collections import defaultdict


class UnionFind:
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


n, m, e = map(int, input().split())
eds = [0] * e
for i in range(e):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    eds[i] = (u, v)
q = int(input())
s = set()
query = []
for _ in range(q):
    x = int(input())
    x -= 1
    s.add(x)
    query.append(x)
ans = [-1] * q
uf = UnionFind(n + m + 1)  # 仮想頂点を１つ作り、そこを電力源とする
for i in range(n, n + m):
    uf.unite(i, n + m)
for i, (u, v) in enumerate(eds):
    if i not in s:
        uf.unite(u, v)
ans[-1] = uf.size(n + m) - m - 1
for i in range(q - 1, 0, -1):
    u, v = eds[query[i]]
    if uf.same(u, v):
        ans[i - 1] = ans[i]
        continue
    if uf.same(u, n + m):
        ans[i - 1] = ans[i] + uf.size(v)
    elif uf.same(v, n + m):
        ans[i - 1] = ans[i] + uf.size(u)
    else:
        ans[i - 1] = ans[i]
    uf.unite(u, v)
for i in range(q):
    print(ans[i])
