#Email validation by python


Email=input("Enter your Email :") # closest condtn=g@g.in
k,j,d=0,0,0
if len(Email)>=6:
    if Email[0].isalpha():  # isalpha for alph condition check
        if ('@'in Email) and (Email.count('@')==1):
            if (Email[-4]==".") ^ (Email[-3]=="."):
                for i in Email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if  i==i.upper():
                            j=1 
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue 
                        else: 
                            d=1  
                if k==1 or j==1 or d==1:
                    print(" Wrong Email") 

            else:
                print("please valdate email again")

            
        else:
            print("Please check @ in given Email id")

    else:
        print("Initial of email must be alphbetic")

else:
    print("Email is not valid")
