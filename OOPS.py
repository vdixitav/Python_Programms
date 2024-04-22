# create calss with property 'var1'

# class myclass:
#     var1=10 # Docstring

# obj1=myclass() # creating an object for class myclass()
# print(obj1.var1) 

# create employee class

class Employee:
    def __init__(self,name ,empid): #__init functn is used to assigning the values
        self.name=name
        self.empid=empid

    def greet(self): # class method
        print("thanks for joining ABC company{}!!".format(self.name))
emp1=Employee("dixita",'90')# create an employee ojbect

print("name",emp1.name)
print("emp1",emp1.empid)

emp1.greet()

