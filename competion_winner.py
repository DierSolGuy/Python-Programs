# Write a program to create a dictionary containing names of competition winner students as keys and number
# of their wins as values

n = int(input(" How many students ? "))
compwinners={}
for i in range(n):
    key=input("Name of the student: ")
    value=int(input("Number of competitions won: "))
    compwinners[key]=value
print("The dictionary now is: ")
print(compwinners)

