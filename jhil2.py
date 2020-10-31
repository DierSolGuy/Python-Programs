#s=x-x^2/2!+x^3/3!....n terms
import math
n=int(input("Enter the value of n:"))
x=int(input("Enter the value of x:"))
sum=0
multi=sign=1
for i in range(1,n+1):  #term generation
    for j in range(1,i+1):  # Factorial section
        multi=multi*j
    sum=sum+sign*((math.pow(x,i))/multi)
    sign*=(-1)
    multi=1
print(sum)    