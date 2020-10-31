import math
x=int(input("Enter the Base: "))
n=int(input("Enter the Exponent: "))
s=0
for i in range(0,n+1):
    s=s+math.pow(x,i)
print("Sum of the series: ",s,end='')