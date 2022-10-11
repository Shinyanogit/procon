import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
eds = [set() for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    eds[U].add(V)
    eds[V].add(U)
C = [[0] * N for _ in range(50)]
for i in range(N):
    for j in range(50):
        for u in eds[i]:
            C[j][i] += A[u]
ng = -10
ok = sum(A) + 100
k = 0
while abs(ok - ng) > 1:
    mid = (ng + ok) // 2
    todo = []
    cost = C[k]
    cnt = 0
    for i in range(N):
        if cost[i] <= mid:
            cnt += 1
            todo.append(i)
    while len(todo) > 0 and cnt < N:
        v = todo.pop()
        for u in eds[v]:
            if cost[u] <= mid:
                continue
            cost[u] -= A[v]
            if cost[u] <= mid:
                cnt += 1
                todo.append(u)
            if cnt == N:
                break
    if cnt == N:
        ok = mid
    else:
        ng = mid
    k += 1
print(ok)
