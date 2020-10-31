import math
n=int(input("Enter the Limit: "))
sum=0
for i in range(0,n+1):
    sum=sum+math.pow(10,i)
    print(int(sum),end=",")
