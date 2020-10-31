# Write a program in python to check whether a number is Perfect Number or not.
n=int(input('Enter a number to check for a perfect number :- '))
sum=0
x=n//2
for i in range(1,x+1):
    if(n%i==0):
        sum+=i
if(n==sum):
    print(n,' is Perfect number')
else:
    print(n,' is not perfect number')