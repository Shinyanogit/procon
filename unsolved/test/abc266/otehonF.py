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


n = int(input())
uf = UnionFind(n)
flg = False  # このufは使い捨て
eds = [set() for _ in range(n)]
for i in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if flg:
        eds[u].add((v, i))
        eds[v].add((u, i))
        continue
    elif uf.same(u, v):
        s_del = u
        g_del = v
        dels = {i}
        flg = True
    else:
        uf.unite(u, v)
        eds[u].add((v, i))
        eds[v].add((u, i))
todo = [s_del]
pastroad = [-1] * n
pastnode = [-1] * n
while len(todo) > 0 and pastroad[g_del] == -1:
    v = todo.pop()
    for u, i in eds[v]:
        if pastroad[u] != -1:
            continue
        pastroad[u] = i
        pastnode[u] = v
        todo.append(u)
# print(pastroad,pastnode)
k = g_del
while k != s_del:
    dels.add(pastroad[k])
    k = pastnode[k]
# print(dels)
uf = UnionFind(n)  # こっちが真打
for u in range(n):
    for v, i in eds[u]:
        if i not in dels:
            uf.unite(u, v)
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if uf.same(x, y):
        print("Yes")
    else:
        print("No")
