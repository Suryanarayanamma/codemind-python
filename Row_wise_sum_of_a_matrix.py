r,c=map(int,input().split())
mat=[]
for l in range(r):
    k=list(map(int,input().split()))
    mat.append(k)
n=[]
for i in range(r):
    s=0
    for j in range(c):
        s=s+mat[i][j]
    n.append(s)
print(*n)