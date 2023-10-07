a=int(input())
b=int(input())
for i in range(a,b+1):
    k=i
    while k:
        r=k%10
        if r==0:
            break
        if i%r!=0:
            break
        k=k//10
    else:
        print(i,end=' ')