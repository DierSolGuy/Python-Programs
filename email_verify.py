email=input("Enter the Email address: ")
domain="@gmail.com"
lemail=len(email)
ldomain=len(domain)
sub=email[lemail-ldomain:]
if (sub==domain):
    if(lemail!=ldomain):
        print(email," is a valid email address")
    else:
        print(email," is not a valid email address")
else:
     print(email,"Email Address exists from different domain. ")