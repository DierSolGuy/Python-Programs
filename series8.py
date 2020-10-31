# print the series 0,7,26,63.... n terms
import math
n=int(input("Enter the limit: "))
for i in range(1,n+1):
    print(int(math.pow(i,3))-1,end=",")