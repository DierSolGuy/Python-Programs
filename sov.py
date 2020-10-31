#s=1/2+3/4+5/6+...+19/20
import math
n=int(input("enter the limit= "))
s=0
for i in range(1,n+1):
    s=s+(((i*2)-1)/(i*2))
print("Sum of the series= ",s)
