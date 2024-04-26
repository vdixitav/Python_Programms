print("Welcome to my computer quiz!!")

playing=input("Do you want to play? ")
print(playing)



if playing.lower() != "yes":
    quit()
print("Okay ! lets play")
score= 0

answer= input("What does CPU stands for ? ")
if answer.lower() =="Central processing unit":
    print("wow !! thats correct")
    score +=1
    

else:
    print("Ohhh !! lets try again") 




answer= input("What does GPU stands for ? ")
if answer.lower() =="Graphic processing unit":
    print("wow !! thats correct")
    score +=1

else:
    print("Ohhh !! lets try again")  



answer= input("What does ROM stands for? ")
if answer.lower() =="Read Only Memory":
    print("wow !! thats correct")
    score +=1

else:
    print("Ohhh !! lets try again") 

print("You got "+str(score)  +" Que are correct !")       