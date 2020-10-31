# Write a program to print triangle '*' pattern according to given limit by user 
n=int(input('Enter a limit:- '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print('\n',end='')