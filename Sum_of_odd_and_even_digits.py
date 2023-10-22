n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if i%2==0:
        s=s+l[i]
    else:
        s1=s1+l[i]
if abs(s-s1)==0:
    print("YES")
else:
    print("NO")