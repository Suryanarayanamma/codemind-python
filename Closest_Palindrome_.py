def is_palindrome(n):
    q=n
    s=0
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
n1=n+1
while n1>0:
    if is_palindrome(n1):
        an=n1
        break
    else:
        n1=n1+1
    
bn=0
n2=n-1
while n1>0:
    if is_palindrome(n2):
        bn=n2
        break
    else:
        n2=n2-1
if abs(n-bn)>abs(n-an):
    print(an)
elif abs(n-bn)<abs(n-an):
    print(bn)
else:
    print(bn,an)