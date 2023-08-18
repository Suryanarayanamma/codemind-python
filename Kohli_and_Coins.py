a=int(input())
if(a%5==0 or a%10==0):
    x=a//10
    y=a%10
    z=y//5
    c=x+z
    print(c)
else:
    print(-1)