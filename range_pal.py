a=int(input('Enter the Lower limit:- '))
b=int(input('Enter the Upper limit:- '))
for i in range(a,b+1):
    reverse=int(str(i)[::-1]) #Slicing Technique
    if i==reverse:
        print(i,' is Palindrome Number')
    else:
        #print(i,' is not Palindrome Number')
        continue
        