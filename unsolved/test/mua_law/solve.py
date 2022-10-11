# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/arc054/tasks/arc054_b
p=float(input())
left=0#
right=p
import math
mid_list=[]
def calc_time(x):#x年後に始めた場合終わる年
    return x+p*math.pow(2,-x/1.5)
def calc_division(x):#calctimeの一次導関数で、負から正に変化
    dt=math.pow(10,-8)
    return (calc_time(x+dt)-calc_time(x-dt))/2*dt
while right-left>(10**-8)*right:
    print(left,right)
    mid=(left+right)/2
    if calc_division(mid)>0:
        right=mid
    else:
        left=mid
    mid_list.append(mid)
    if right==0:
        break
print(calc_time(mid))
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,p,1000)
plt.plot(x,np.array([calc_time(each_x) for each_x in x]))
plt.scatter(mid_list,[calc_time(mid) for mid in mid_list])
plt.show()