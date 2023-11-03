r=int(input())
mat1=[]
mat2=[]
for l in range(r):
    k=list(map(int,input().split()))
    mat1.append(k)
for m in range(r):
    g=list(map(int,input().split()))
    mat2.append(g)
n=[]
for i in range(r):
    e=[]
    for j in range(r):
        s=mat1[i][j]+mat2[i][j]
        e.append(s)
    n.append(e)
for d in n:
    for c in d:
        print(c,end=' ')
    print()
    