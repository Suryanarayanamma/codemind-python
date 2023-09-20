def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def is_palindrome(n):
    s=0
    q=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if (s==q):
        return True
    else:
        return False
def next_palindrome(n):
    an=0
    n1=n+1
    while n1>0:
        if is_palindrome(n1) and is_prime(n1):
            an=n1
            break
        else:
            n1=n1+1
    return an
n=int(input())
print(next_palindrome(n))