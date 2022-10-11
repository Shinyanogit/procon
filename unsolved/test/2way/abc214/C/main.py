n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = [0 for i in range(n)]
mt = min(t)
idx0 = t.index(mt)
ans[idx0] = mt
idx = (idx0 + 1) % n
while idx != idx0:
    ans[idx] = min(ans[idx - 1] + s[idx - 1], t[idx])
    idx += 1
    idx %= n
for i in range(n):
    print(ans[i])
