n=input("Enter the String: ")
count1=count2=count3=count4=0
for a in n:
    if (a.isupper()):
        count1+=1
    if (a.islower()):
        count2+=1
    if (a.isdigit()):
        count3+=1
    if (a.isalpha()):
        count4+=1
print("Number of the Uppercase Letters: ",count1)
print("Number of the Lowercase Letters: ",count2)
print("Number of the Digit: ",count3)
print("Number of the Alphabets: ",count4)