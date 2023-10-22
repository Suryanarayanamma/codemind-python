n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i%2==0:
        k.append(i)
if len(k)==n:
    print("True")
else:
    print('False')