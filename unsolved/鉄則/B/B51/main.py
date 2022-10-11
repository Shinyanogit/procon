from collections import deque

left = deque()
S = input()
for i in range(len(S)):
    # ペアができるたびに出力していく
    character = S[i]
    if character == "(":
        left.append(i + 1)
    elif character == ")":
        l = left.pop()
        print(f"{l} {i+1}")
