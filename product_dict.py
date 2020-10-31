n = int(input(" How many Products ? "))
product={}
for i in range(n):
    key=input("Name of the Product: ")
    value=int(input("Number of Prices: "))
    product[key]=value
    
key1=input(" Enter product: ") 
for i in product:
    if (key1 not in product):
        print(" Product not found")
        break
        
    else:
        print(" Product found")
        print(product[i])
        break


