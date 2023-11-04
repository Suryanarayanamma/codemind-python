r,c=map(int,input().split())
mat=[]
for l in range(r):
    k=list(map(int,input().split()))
    mat.append(k)
n=[]
for i in range(c):
    s=0
    for j in range(r):
        s=s+mat[j][i]
    n.append(s)
print(max(n))