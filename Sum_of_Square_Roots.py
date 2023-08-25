a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    s=s+(i**0.5)
print(f"{s:0.2f}")