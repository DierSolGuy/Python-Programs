# Write a program to print a string in described order
n=input('Enter a String:- ')
x=0
for i in range(-1,-(len(n))-1,-1):
    print(n[x],n[i],sep='\t')
    x=x+1