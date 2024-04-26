# create calss with property 'var1'

# class myclass:
#     var1=10 # Docstring

# obj1=myclass() # creating an object for class myclass()
# print(obj1.var1) 

# create employee class

# class Employee:
#     def __init__(self,name ,empid): #__init functn is used to assigning the values
#         self.name=name
#         self.empid=empid

#     def greet(self): # class method
#         print("thanks for joining ABC company{}!!".format(self.name))
# emp1=Employee("dixita",'90')# create an employee ojbect

# print("name",emp1.name)
# print("emp1",emp1.empid)

# emp1.greet()


# emp1.name='bhakti' # odify object property
# print(emp1.name)


#####Inheritance####

# class person:  # parent class
#     def __init__(self, name , age ,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender


#     def personalInfo(self) :
#         print('Name :',format(self.name))
#         print('Age :',format(self.age))
#         print('Gender :',(self.gender))


# class student(person): # child class
#     def __init__(self,name,age,gender,studentid,fees):
#         person.__init__(self,name,age,gender)
#         self.studentid=studentid
#         self.fees=fees

#     def StudentInfo(self):
#         print('Student id :'.format(self.studentid))
#         print('fees :'.format(self.fees))


#     class teacher(person): # child class

#         def __init__(self, name, age, gender,empid,salary):
#             person.__init__(self,name,age,gender)
#             self.empid=empid
#             self.salary=salary

#         def TeacherInfo(self):
#             print("empyee id:".format(self.empid))
#             print("salary".format(self.salary))

# stud1=student('dixita','24','male',123,1200)    
# print('Student details')
# print('-----')
# stud1.personalInfo()
# stud1.StudentInfo()
# print()            


        





#Multi level inheritance

# class person: # parent class
#     def __init__(self,name,age,gender) :
#         self.name=name
#         self.age=age
#         self.gender=gender

#     def PersonInfo(self):
#         print("name:".format(self.name))
#         print('Age :'.format(self.age))
#         print('Gender:'.format(self.gender))


# class employee(person): # child class
#     def __init__(self,name,age,gender,empid,salary):
#         person.__init__(self,name,age,gender)
#         self.empid=empid
#         self.salary=salary

#     def employee(self):
#         print('empid:'.format(self.empid))
#         print('salary:'.format(self.salary))  


# Multiple Inheritance

 # Super class

# class Father:
#     def __init__(self) -> None:
#         self.fathername=str()


#  # Super class

# class Mother:
#     def __init__(self) -> None:
#         self.mothername=str()

#  # sub class 

# class Son(Father,Mother):
#     Name=str()
#     def show(self):
#         print("my name :",self.Name)
#         print("My father's name:",self.fathername)
#         print("My mother's name:",self.mothername)

# s1=Son()
# s1.fathername="vilas"
# s1.mothername="Jyoti"
# s1.show()


## Override ###

class person: # parent class
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def greet(self):
        print("Hello person")

        
            
        





        