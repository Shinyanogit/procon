from time import time
start=time()
import sys
input=sys.stdin.readline
N,T=map(int,input().split())
T_ways=0
def ways(val1,val2,val3):
    way=1
    if val1==1:
        way*=2
    if val2==1:
        way*=2
    if val3==1:
        way*=2
    return way
def gcd(x,y):
    if x==0:
        return y
    else:
        a=y%x
        b=x
        return gcd(a,b)
if T<N+2:
    upper1=T-2
else:
    upper1=N
for value1 in range(1,upper1+1):
    if T-value1<N+1:
        upper2=T-value1-1
    else:
        upper2=N
    for value2 in range(1,upper2+1):
        value3=T-value1-value2
        if value3<=N:
            T_ways+=ways(value1,value2,value3)
all_ways=(N+1)**3
g=gcd(T_ways,all_ways)
bunshi=str(T_ways/g)
bunbo=str(all_ways/g)
print(bunshi+"/"+bunbo)
print(time()-start)