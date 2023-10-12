n=int(input())
k=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if k[i]%2!=0:
        s=k[i]
        break
print(s)