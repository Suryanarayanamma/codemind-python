n=int(input())
k=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if k[i]==s:
        c=c+1
print(c)