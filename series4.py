import math
n=int(input("Enter the Limit: "))
sum=0
multi=1
for i in range(1,n+1): 
    for j in range(1,i+1): # factorial calculation
        multi=multi*j
    sum=sum+multi
    multi=1     #reinitialisation
print("sum of the series: ",sum,end="")
    