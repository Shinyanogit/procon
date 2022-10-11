# -*- coding: utf-8 -*-
import sys
input=sys.stdin.readline
n=int(input())
A=[list(input())[:-1] for i in range(n)]
print(A)
def trueornot(x,y):
    if (x,y) in [("W","L"),("D","D"),("L","W"),("-","-")]:
        return True
    else:
        return False
for i in range(n-1):#i（0からn-2）人目の人の勝敗をチェックする
    for j in range(i+1,n):#j(i+1からn-1まで)人目の相手とのマッチを確認
        if not trueornot(A[i][j],A[j][i]):
            print("incorrect")
            exit()
print("correct")
