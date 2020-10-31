# S=(1/x)+(2/x^2)+(3/x^3)+(4/x^4)+....N terms
import math
n=int(input("Enter limit: "))
x=int(input("Enter value of x:"))
sum=0
for i in range(1,n+1):
    sum=sum+(i/math.pow(x,i))
print(sum)
