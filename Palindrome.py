n=int(input())
s=0
q=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if(q==s):
    print("Palindrome")
else:
    print("Not Palindrome")