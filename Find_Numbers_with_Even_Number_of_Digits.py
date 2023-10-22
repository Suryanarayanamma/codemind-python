n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    s=str(i)
    if len(s)%2==0:
        k.append(i)
print(len(k))