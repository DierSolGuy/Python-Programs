a=int(input('Enter the Lower Limit:- '))
b=int(input('Enter the upper Limit:- '))
x=0
y=1
z=0
print(x,y,sep=' ',end=' ')
for i in range(a,b-1):
    z=x+y
    print(z,sep=' ',end=' ')
    x=y
    y=z