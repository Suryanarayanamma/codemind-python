a,b,c=map(int,input().split())
if(a>b and c>b):
    print(a+c)
elif(b>c and a>c):
    print(a+b)
else:
    print(b+c)