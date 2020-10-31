# print the series: 0,3,8,15,...n terms
import math
n=int(input("enter the limit: "))
for i in range(1,n+1):
    print (int((math.pow(i,2))-1),sep=" ",end=",")