import sys

sys.setrecursionlimit(250000)
input = sys.stdin.readline
dp = []
w =[]

def rec(l,r):
    #既に探索済の場合はその値を返す
    if dp[l][r] >= 0:
        return dp[l][r]

    #単一ケースは落とせないので0
    if l == r:
        dp[l][r] = 0
        return 0

    #連続している箇所の場合
    if l + 1 == r:
        if abs(w[l] - w[r]) <= 1:
            dp[l][r] = 2
            return 2
        else:
            dp[l][r] = 0
            return 0

    res = 0

    #Case1 両端に挟まれている箇所がすべて消えて、さらに残った両端が消える
    if abs(w[l] - w[r]) <= 1 and rec(l+1, r-1) == (r - 1) - (l + 1) + 1:
        res =  (r - 1) - (l + 1) + 1 + 2
    else: #Case2 両端に挟まれている箇所が消えない
        for mid in range(l,r):
            res = max(res, rec(l,mid)+rec(mid+1,r))

    dp[l][r]=res
    return res
def main():
    global w
    global dp
    n_list=[]
    w_list=[]

    while True:
        n = int(input())
        if n == 0 :
            break
        w_tmp = list(map(int, input().split()))
        n_list.append(n)
        w_list.append(w_tmp)

    for i in range(len(n_list)):
        dp = [[-1] * n_list[i] for j in range(n_list[i])]
        w = w_list[i]
        print(rec(0,n_list[i]-1))
main()
