n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if k[i-1]%2==0 and k[i]%2!=0 and k[i+1]%2==0:
        c=c+1
print(c)