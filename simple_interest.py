# Write a program by using interest funtion to calculate simple interest and return SI value and also using
# different values from the actual parameter.

def simple(p,t,r):  #formal Parameter
    si=(p*r*t)/100.0
    return si
#_____main function_____
x=int(input("Enter the principal: "))
y=int(input("Enter the time: "))
z=float(input("Enter the rate: "))
p=simple(x,y,z)
c=simple(100,2.0,0.9) # Actual parameter
d=simple(1000,3.0,0.09) # Actual parameter
e=simple(10000,3.0,0.07) # Actual parameter

print("Simple Interest",p)
print("Simple Interest",c)
print("Simple Interest",d)
print("Simple Interest",e)
