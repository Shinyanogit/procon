h, w, k = map(int, input().split())
save_data = [list(map(int, input().split())) for i in range(h)]
position = save_data.copy()
#はいゴミ

def show():
    for line in position:
        print(line)


def rotate(t):  # positionをtが一なら右に傾け、違えばもとに戻す
    global position
    if t:  # 右に傾ける
        result = [[0] * h for i in range(w)]
        show()
        for i in range(h):
            for j in range(w):
                print(w, h, j, h - i - 1, i, j)
                result[j][h - 1 - i] = position[i][j]
        position = result
    else:  # もとに戻す
        result = [[0] * w for i in range(h)]
        for i in range(w):
            for j in range(h):
                result[h - 1 - j][i] = position[i][j]

        position = result


def move_to_left(some_list):
    result = [0 for i in range(len(some_list))]
    index_counter = 0
    for num in some_list:
        if num:
            result[index_counter] = num
            index_counter += 1
    return result


def fall():
    # 各列についてどんどん落下させていく
    # そのために右に傾けてから左に詰めていく
    global position
    rotate(1)
    for i in range(w):  # i行目を左詰めしていく
        position[i] = move_to_left(position[i])
    rotate(0)  # 左に傾けて元通り


def banish():  # kつ以上並んだ箇所を特定して削除,出力には結果と点数
    global position
    result = position.copy()
    score = 0
    if k <= w:  # 横で消す
        for i in range(h):  # i行目を考える
            row = position[i]
            for length in reversed(range(k, w + 1)):  # 長さがw-kまでで該当する箇所を削除していく
                for start in range(w - length + 1):
                    tmp = list(set(row[start : start + length]))
                    if len(tmp) == 1 and (0 not in tmp):
                        score += length * tmp[0]
                        for j in range(length):
                            result[i][start + j] = 0
    return (result, score)


max_score = 0
for i in range(h):
    for j in range(w):  # 最初に消すコマが(i,j)
        tot_score = 0
        position = save_data.copy()  # 初期化
        position[i][j] = 0  # 最初のドミノを倒す
        counter = 1
        fall()
        position, score = banish()
        tot_score += score
        counter *= 2
        while score:  # 前の段階で消えた
            fall()
            position, score = banish()
            tot_score += score
            counter *= 2
        max_score = max(max_score, tot_score)
print(max_score)
