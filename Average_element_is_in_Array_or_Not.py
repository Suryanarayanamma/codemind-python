n=int(input())
k=list(map(int,input().split()))
l=sum(k)//n
print(l in k)