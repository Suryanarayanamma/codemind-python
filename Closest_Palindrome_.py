def is_palindrome(n):
    s=0
    q=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==q:
        return True
    else:
        return False
n=int(input())
an=0
bn=0
n1=n+1
while n1>0:
    if is_palindrome(n1):
        an=n1
        break
    else:
        n1=n1+1
n2=n-1
while n1>0:
    if is_palindrome(n2):
        bn=n2
        break
    else:
        n2=n2-1
d1=an-n
d2=n-bn
if(d1==d2):
    print(bn,an)
elif(d1>d2):
    print(bn)
else:
    print(an)