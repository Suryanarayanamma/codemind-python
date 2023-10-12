n=int(input())
num=list(map(int,input().split()))
s=0
for i in range(1,n):
    s=s+i
avg=s//n
if avg in num:
    print("True")
else:
    print("False")