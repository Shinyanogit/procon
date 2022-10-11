N = int(input())


def create_kakko(left, right, history):  # 余分に（がある状態から右に規則を守って付け足して、辞書順に吐き出す
    if left == 0 and right == 0:  # 終わり
        print(history)
        return
    if left - right == 0:  # rightを吐けない
        create_kakko(left - 1, right, history + "(")
        return
    # どっちも吐ける
    if left:  # leftがまだ打てる
        create_kakko(left - 1, right, history + "(")
    if right:  # rightがまだ打てる
        create_kakko(left, right - 1, history + ")")


if N % 2:
    exit()
create_kakko(N / 2, N / 2, "")
