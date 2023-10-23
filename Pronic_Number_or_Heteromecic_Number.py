n=int(input())
f=False
for i in range(1,n+1):
    if i*(i+1)==n:
        f=True
        break
if f==True:
    print("YES")
else:
    print("NO")