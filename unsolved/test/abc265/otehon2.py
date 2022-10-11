n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
cums=set()
sum=0;cums.add(0)
for ai in a: sum+=ai;cums.add(sum)
for u in cums:
  if u+p in cums and u+p+q in cums and u+p+q+r in cums:
    print("Yes");exit()
print("No")
