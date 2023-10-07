n=int(input())
a=0
b=1
fb=1
while fb<n:
    a=b
    b=fb
    fb=a+b
if(abs(fb-n)==abs(b-n)):
    print(b,fb)
elif(abs(fb-n)>abs(b-n)):
    print(b)
else:
    print(fb)