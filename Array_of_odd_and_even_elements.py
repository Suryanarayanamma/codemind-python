n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if i%2!=0:
        l.append(i)
for i in k:
    if i%2==0:
        l.append(i)
for j in l:
    print(j,end=' ')