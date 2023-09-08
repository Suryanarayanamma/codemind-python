d,c=map(int,input().split())
a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
x=a1+a2+a3
y=b1+b2+b3
if(x>=150 and y>=150):
    k=x+y+d+d
    l=x+y+c
    if(k>l):
        print("YES")
    else:
        print("NO")
elif(x>=150 and y<150):
    p=x+y+d
    q=x+y+c
    if(p>q):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    