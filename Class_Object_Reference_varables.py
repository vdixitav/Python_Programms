
class Student:
    def __init__(self,x,y,z) -> None:
        self.name='python'
        self.rollno=000
        self.marks=x

    def talk(self):
        print("Hello there,My name is",self.name)
        print("My roll no",self.rollno)
        print("My marks",self.marks)

s1=Student("",101,80)

print(s1.name,s1.rollno,s1.marks)





# print("S1:",s1.name)
# s2=Student()
# print("S2",s2.name)

# print('Adress of s1',id(s1))
# print("Adress of s2",id(s2))


# print(s.marks)
# print(s.name)
# print(s.rollno)

# s.talk()

