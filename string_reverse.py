# Write a program to print a string reverse horizontally
n=input('Enter a String:- ')
for i in range(-1,-(len(n))-1,-1):
    print(n[i],sep=' ',end='')