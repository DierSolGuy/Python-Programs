# Write a program in python to check whether a number is prime or composite.
n=int(input('Enter a number to be checked for Prime Number or not:- '))
if (n==1):
    print("1 is neither prime nor composite")
else:
    c=0
    i=2
    x=n//2
    while(i<=x):
        if(n%i==0):
            c=c+1
        i=i+1
    if(c==0):
        print(n,' is prime number')
    else:
        print(n,' is Composite number')