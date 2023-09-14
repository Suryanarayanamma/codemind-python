def reverse(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input())
sq=n*n
rev=reverse(n)
sq1=rev*rev
if sq==reverse(sq1):
    print('True')
else:
    print('False')