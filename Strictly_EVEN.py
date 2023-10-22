n=int(input())
l=list(map(int,input().split()))
k=[]
s=[]
for i in range(n):
    if i%2==0 and l[i]%2==0:
        k.append(i)
for i in l:
    if i%2==0:
        s.append(i)
if len(k)==len(s):
    print('True')
else:
    print("False")