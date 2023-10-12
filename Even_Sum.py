n=int(input())
num=list(map(int,input().split()))
s=0
for i in num:
    if(i%2==0):
        s=s+i
print(s)