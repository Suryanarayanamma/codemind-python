r,c=map(int,input().split())
mat=[]
for l in range(r):
    k=list(map(int,input().split()))
    mat.append(k)
s=0
for i in mat:
    for j in i:
            s=s+j
print(s)