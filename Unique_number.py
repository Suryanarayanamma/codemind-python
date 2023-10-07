n=int(input())
l=[]
c=0
while n>0:
    r=n%10
    c=c+1
    if r not in l:
        l.append(r)
    n=n//10
if c==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")