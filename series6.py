import math
n=int(input("Enter the Limit: "))
c=sum=sum1=sum2=0
for i in range(0,n):
    sum=sum+math.pow(10,i)
    sum1+=sum
    sum2+=sum1
    print(int(sum1),end=",")
    
print("\n")
print("Sum of the series: ",int(sum2),end="")
