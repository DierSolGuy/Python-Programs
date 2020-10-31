# S = (1-a/2)+(3-a/4)+(5-a/6)+......to n terms
import math
n=int(input("Enter the limit: "))
a=int(input("Enter the value of a: "))
k=2
y=1
sum=0
for i in range(1,n+1):
    sum=sum+(y-(a/k))
    k+=2
    y+=2
print(sum)
