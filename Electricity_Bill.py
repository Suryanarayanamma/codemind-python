u=int(input())
if u<=199:
    c=1.20
elif u>=200 and u<400:
    c=1.40
elif u>=400 and u<600:
    c=1.60
elif u>=600 and u<800:
    c=1.80
else:
    c=2.00
b=u*c
if(b>=400):
    sc=0.15*b
else:
    sc=0
ta=b+sc
print(f"Units Consumed: {u}",end='
')
print(f"Cost per Unit: {c:.2f}",end='
')
print(f"Bill: {b:.2f}",end='
')
print(f"Surcharge: {sc:.2f}",end='
')
print(f"Total Amount: {ta:.2f}")