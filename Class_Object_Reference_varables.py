
class Student:
    def __init__(self) -> None:
        self.name="Python"
        self.rollno=101
        self.marks=80

    def talk(self):
        print("Hello there,My name is",self.name)
        print("My roll no",self.rollno)
        print("My marks",self.marks)

s=Student()

print(s.marks)
print(s.name)
print(s.rollno)

s.talk()

