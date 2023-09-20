def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def nearest_prime(n):
    if is_prime(n):
        return 0
    an=0
    bn=0
    n1=n+1
    while n1>0:
        if is_prime(n1):
            an=n1
            break
        else:
            n1=n1+1
    n2=n-1
    while n2>0:
        if is_prime(n2):
            bn=n2
            break
        else:
            n2=n2-1
    d1=an-n
    d2=n-bn
    return min(d1,d2)
n=int(input())
print(nearest_prime(n))