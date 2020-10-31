n=int(input('Enter a limit:- '))
for i in range(1,n+1):
    for sp in range(n,i,-1):  # space loop
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n',end='')
for i in range(n-1,0,-1):
    for sp in range(n,i,-1):  # space loop
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n',end='')