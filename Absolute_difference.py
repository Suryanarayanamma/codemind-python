def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
s=1
s1=1
for i in l:
    if is_prime(i):
        s=s*i
    else:
        s1=s1*i
print(abs(s-s1))
        