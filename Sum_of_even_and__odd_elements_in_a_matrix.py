r,c=map(int,input().split())
mat=[]
for l in range(r):
    k=list(map(int,input().split()))
    mat.append(k)
s=0
s1=0
for i in mat:
    for j in i:
        if j%2==0:
            s=s+j
        else:
            s1=s1+j
print(s,s1)