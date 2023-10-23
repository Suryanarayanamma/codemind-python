def is_reverse(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
sq=n*n
x=is_reverse(n)
sq1=x*x
if sq==is_reverse(sq1):
    print("True")
else:
    print("False")