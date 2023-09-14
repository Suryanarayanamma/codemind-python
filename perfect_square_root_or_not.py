n=int(input())
flag=False
for i in range(n):
    if(i*i==n):
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("True")
else:
    print("False")