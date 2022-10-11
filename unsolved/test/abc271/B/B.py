N, Q = map(int, input().split())
arrays = [list(map(int, input().split())) for i in range(N)]
for i in range(Q):
    s, t = map(int, input().split())
    print(arrays[s - 1][t])
