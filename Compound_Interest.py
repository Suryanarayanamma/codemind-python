import math
p=int(input())
r=int(input())
t=int(input())
ci=p*pow((1+r/100),t)-p
print(f"{ci:.2f}")