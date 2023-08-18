u=int(input())
if u<=199:
    c=1.20
elif u>=200 and u<400:
    c=1.50
elif u>=400 and u<600:
    c=1.80
else:
    c=2.00
b=u*c
if(b>=400):
    sc=0.15*b
else:
    sc=100
cb=b+sc
print(f"{cb:.2f}")