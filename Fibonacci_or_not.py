n=int(input())
a=0
b=1
c=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        a=b
        b=c
    if c==n:
        print("True")
    else:
        print("False")
