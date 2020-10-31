# S=(x/1)+(x/4)+(x/7)...n terms
import math
n=int(input("Enter the limit: "))
x=int(input("Enter the value of numerator: "))
sum=0
k=1
for i in range(1,n+1):
    sum=sum+(x/k)
    k+=3
print(sum)