n=int(input(" Enter the Limit: "))
for i in range((n-1),0,-1):
    for j in range(1,i+1):
        print('*', end='')
    print('\n',end='')
    