n=int(input('Enter a limit:- '))
for i in range(1,n+1):
    for sp in range(5,i,-1):  # space loop
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print('\n',end='')