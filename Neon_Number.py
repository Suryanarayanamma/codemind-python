n=int(input())
sq=n*n
q=sq
s=0
while(q>0):
    r=q%10
    s=s+r
    q=q//10
if(n==s):
    print("Neon Number")
else:
    print("Not Neon Number")