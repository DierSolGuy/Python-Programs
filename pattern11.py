n=int(input('Enter a limit:- '))
c=0
for i in range(1,n+1):  #Row 
    for j in range(1,i+1):  #column
        print(c,end='')
    print('\n',end='')
    c+=2
