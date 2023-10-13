n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
n=sum(k)
s=0
for i in k:
    if i>=a and i<=b:
        s=s+i
print(n-s)