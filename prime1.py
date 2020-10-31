n=int(input('Enter a number:- '))
c=0
x=n//2
for i in range(2,x+1):
    if(n%i==0):
        c=c+1
if(c==0):
    print(n,' is prime number')
else:
    print(n,' is Composite number')