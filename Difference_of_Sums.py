n=int(input())
s=0
s1=0
for i in range(1,n+1):
    s=s+(i**2)
    s1=s1+i
x=s1**2
print(x-s)