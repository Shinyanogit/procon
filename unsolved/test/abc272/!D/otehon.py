from collections import deque

INF = 1 << 60
N, M = map(int, input().split())
jump = set()
for i in range(-N + 1, N):
    for j in range(-N + 1, N):
        if i**2 + j**2 == M:
            jump.add((i, j))

bfs = [[INF] * N for _ in range(N)]
bfs[0][0] = 0
todo = deque()
todo.append(0)
while len(todo) > 0:
    k = todo.popleft()
    x = k // N
    y = k % N
    b = bfs[x][y]
    for jx, jy in jump:
        if 0 <= x + jx < N and 0 <= y + jy < N and bfs[x + jx][y + jy] > b + 1:
            bfs[x + jx][y + jy] = b + 1
            todo.append((x + jx) * N + y + jy)
for i in range(N):
    for j in range(N):
        if bfs[i][j] == INF:
            bfs[i][j] = -1
for i in range(N):
    print(*bfs[i])
