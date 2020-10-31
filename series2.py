import math
n=int(input("Enter the Limit: "))
s=0
for i in range(1,n+1):
  s=s+math.pow(i,i)
print("Sum of the series: ",(int)(s),end='')