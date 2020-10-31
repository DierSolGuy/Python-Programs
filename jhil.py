#s=1-2+3-4+5......n terms
n=int(input("Enter the limit:"))
sum=0
sign=1
for i in range(1,n+1):
    sum=sum+sign*i
    sign=sign*(-1)
print(sum)    