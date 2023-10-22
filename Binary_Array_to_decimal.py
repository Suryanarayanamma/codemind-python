n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    k=2**(n-1)
    s=s+(i*k)
    n=n-1
print(s)