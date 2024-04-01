class Movie:
    '''Movie class developed by me for python demo purpose'''

    def __init__(self,title,actor,actress) :
        self.title=title
        self.actor=actor
        self.actress=actress





    def info(self):
        print("movie name:",self.title)
        print("actor name:",self.actor)
        print("actress name:",self.actress)

# m=Movie("Open Hymer","SRK","Anushka") 
# m.info()

list_of_movies=[]
while True:
    title=input("Enter movie name:")
    actor=input("Enter movie actor:")
    actress=input("Enter movie actress:")
    m=Movie(title,actor,actress)

    # adding movie object to lst
    list_of_movies.append(m)

    print("movies added to lst successfully")

    option=input("do you wanr to add one more movie [Yes/No]:")
    if option.lower()=="no":
        break

print("All movies info") 
print("#"*40) 

for movie in list_of_movies:
    movie.info()


       
        