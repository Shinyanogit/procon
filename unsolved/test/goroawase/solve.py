#1のゴロ、2のゴロ、3のゴロ、、、kのゴロというふうに登場した数字全てに対応するゴロを列挙したい
#https://atcoder.jp/contests/abc031/tasks/abc031_d
# -*- coding: utf-8 -*-
from itertools import product
n,k=map(int,input().split())
value_list=[]#数字リスト
word_list=[]#ゴロリスト
length=0#もとデータの数字の総長さ
for line in range(k):
    [v,w]=input().split()
    value_list.append(v)
    word_list.append(w)
    length+=len(v)
def xor(a,b):
    return bool(a) != bool(b)
dictionary=dict(zip(list("123456789"),[False for i in range(1,10)]))#これを完成させたい
split_determiners=product([0,1,2],repeat=n)
for split_determiner in split_determiners:#登場する順番に数字にゴロを結びつける。その長さをsplit_determinerの各タプルで決定
    value_list_left=value_list.copy()
    word_list_left=word_list.copy()
    uncompleted_dictionary=dictionary.copy()
    flag=True
    # print(split_determiner)
    flag_debug=list(split_determiner)==[2,1,2,0,1,1]
    for size_minus1 in split_determiner:#新しい文字の探索
        if not flag:
            continue
        if flag_debug:
            print(value_list_left)
            print(word_list_left)
            print(value_list_left+word_list_left)
            print(uncompleted_dictionary)
            print(33)
        # if len(value_list_left+word_list_left)==0:#無事終了
        #     result=uncompleted_dictionary
        #     print("success")
        #     break
        head_value=value_list_left[0][0]#数字リストの先頭
        # if flag_debug:
            # print(value_list_left)
            # print(word_list_left)
            # print(value_list_left+word_list_left)
            # print(uncompleted_dictionary)
        while uncompleted_dictionary[head_value]!=False:#リストの先頭が既存の数字である場合
            # print(1)
            if len(value_list_left+word_list_left)==0:#無事終了
                # result=uncompleted_dictionary
                # print("success")
                break
            goro=uncompleted_dictionary[head_value]
            word=word_list_left[0]
            # print(word_list_left)
            if word.startswith(goro):#ゴロが適合した場合
                if len(word)>len(goro):#ゴロを省いても一文字以上文字が残る
                    word_list_left[0]=word[len(goro):]#ゴロを削る
                    value_list_left[0]=value_list_left[0][1:]#数字を削る
                else:#ゴロを省いたら文字がなくなる
                    if len(value_list_left[0])>2:#数字が無くならない、、？
                        flag=False
                        break
                    else:#数字もなくなる
                        word_list_left=word_list_left[1:]
                        value_list_left=value_list_left[1:]
            else:#予測したゴロが破綻した場合
                flag=False
                break
        #以降、新しいゴロ
        size=size_minus1+1
        value=value_list_left[0]
        word=word_list_left[0]
        value_size=len(value)
        word_size=len(word)
        #まずはvalue_list,word_listを更新する
        # print(size,word_size)
        if word_size>size and value_size>2:#サイズが十分であり、かつ無くなったりしない場合
            value_list_left[0]=value[1:]
            word_list_left[0]=word[size:]
            # print(78)
        elif word_size<size or xor(word_size==size,value_size==1):#サイズが十分でない、または片方のみが無くなってしまう
            flag=False
            print(81)
            # print("word_size,size,value_size",word_size,size,value_size)
            # print("サイズが十分でない、または片方のみが無くなってしまう")
            break
        else:#サイズが十分で同時にサイズがゼロになる
            word_list_left=word_list_left[1:]
            value_list_left=value_list_left[1:]
            # print(87)
        #辞書を更新する
        uncompleted_dictionary[value[0]]=word[:size]
        # if flag_debug:
            # print(uncompleted_dictionary)
    if not flag:
        print(94)
        continue
    print(uncompleted_dictionary,split_determiner)
    # if len(value_list_left+word_list_left)==0 and flag:#無事終了
    #     result=uncompleted_dictionary
    #     print(split_determiner)
    #     # print("success")
    #     break
# print("over")
for s in result.values():
    print(s)