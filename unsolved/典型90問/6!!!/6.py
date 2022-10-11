# -*- coding: utf-8 -*-
# 不連続部分列,,,dpだろ絶対
# あらやだTLE
# 27文字全てについて、i文字目以降で一番左にくるindexを格納した27*nのテーブルを用意する(O(n))
# そのあと頭からi番目の文字を、indexがn-k+i以下の若い文字から有線で選んでいく（O(n）
import sys

INF = 1 << 60
alphabets = list(map(chr, range(97, 123)))
input = sys.stdin.readline
N, K = map(int, input().split())
# 右からi番目までの文字で作れる、j文字の辞書順最小文字列
S = input()[:-1]
exist_alphabets = set(list(S))
exist_code = [ord(s) for s in exist_alphabets]
next_index = []


results = dict(zip(map(chr, range(97, 123)), [[INF] for i in range(26)]))
results[S[-1]] = [N - 1]
counter = N - 1
for s in list(reversed(S))[1:]:
    counter -= 1
    for i in range(26):
        if s == alphabets[i]:
            results[s].append(counter)
        else:
            # print(results[alphabets[i]])
            results[alphabets[i]].append(results[alphabets[i]][-1])
for a in alphabets:
    results[a].reverse()
next_index = results
# print(next_index)
answer = ""
last_index = 0
for i in range(K):  # i番目の文字は次のindexがn-k+i以下のなるべく若い文字
    for j in range(26):
        if next_index[alphabets[j]][last_index] <= N - K + i:
            answer += alphabets[j]
            last_index = next_index[alphabets[j]][last_index] + 1

            break
    # print(next_index["a"])
    # print(next_index["b"])
    # print(next_index["c"])
    # print(next_index["d"])
    # print()
# print(next_index)
print(answer)
