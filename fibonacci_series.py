# Fibonacci Series for a given limit.
n=int(input('Enter a limit:- '))
x=0
y=1
z=0
print(x,y,sep=' ',end=' ')
for i in range(1,n-1):
    z=x+y
    print(z,sep=' ',end=' ')
    x=y
    y=z