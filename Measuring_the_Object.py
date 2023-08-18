w,x,y,z=map(int,input().split())
if(w==x or w==y or w==z or w==x+y or w==y+z or w==z+x):
    print("YES")
else:
    print("NO")