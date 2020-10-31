# S= (1+2/1*2)+(1+2+3/1*2*3)+..... n terms
n=int(input("enter a limit:"))
sum=0
k=2
num=denom=1
for i in range(1,n+1):
    num=num+k
    denom=denom*k
    sum=sum+(num/denom)
    k=k+1
print(sum)
    