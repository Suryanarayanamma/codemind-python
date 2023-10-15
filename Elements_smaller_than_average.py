n=int(input())
k=list(map(int,input().split()))
a=sum(k)//n
c=0
for i in k:
    if i<=a:
        c=c+1
print(c)