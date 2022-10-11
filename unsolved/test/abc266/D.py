N = int(input())
INF = 1 << 60
snukes = [map(int, input().split()) for i in range(N)]
dp = [[0, -INF, -INF, -INF, -INF]]  # ti成分が、t匹目時点でiにいる人の、その時点での最高点
time = 0


def update(
    log, time_delta, index, size
):  # logを元に、time_delta秒後にindexにsizeのすぬけが出現するとしたときの各地点での最終スコアの最大値をreturn
    # print(log, time_delta, index, size)
    answer = log.copy()
    for i in range(5):  # i成分について
        max_size = log[i]
        for j in range(5):  # jスタート
            if abs(j - i) <= time_delta:  # 間に合う
                if i == index:
                    if size + log[j] > max_size:
                        max_size = size + log[j]
                else:
                    if log[j] > max_size:
                        max_size = log[j]
        answer[i] = max_size
    return answer


for next_time, index, size in snukes:
    time_delta = next_time - time
    answer = update(dp[-1], time_delta, index, size)
    time = next_time
    # print(answer)
    dp.append(answer)
print(max(dp[-1]))
