import random
top_of_range= input("Type a number :")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

if top_of_range <=0: 
    print("Please type a number larger than zero")   
    quit() 

else:
    print("please type a number next time")    
random_number=random.randint(0,top_of_range)


while True:
   user_guess=input("make a guess :")
   if user_guess.isdigit():
       user_guess=int(user_guess)
   else :  

       print("please type number next time")   

