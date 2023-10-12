n=int(input())
k=list(map(int,input().split()))
s1=0
s2=0
for i in k:
    if i%2==0:
        s1=s1+i
    else:
        s2=s2+i
print(abs(s1-s2))