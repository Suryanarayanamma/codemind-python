n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i==0 or i==1:
        k.append(i)
if len(k)==n:
    print("True")
else:
    print("False")