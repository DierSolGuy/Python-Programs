n=int(input('Enter a Number:- '))
x=0
y=1
z=0
#print(x,y,sep=' ',end=' ')
while(z<n):
    z=x+y
    x=y
    y=z
if(n==z):
    print(n,' is Fibonacci number')
else:
    print(n,' is not Fibonacci number')