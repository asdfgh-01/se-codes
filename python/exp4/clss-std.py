class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
            print("Name: ",self.name,"\nRoll number: ",self.roll_no,"\nAge: ",self.age,"\nMarks: ",self.marks)
    def setAge(self):
        self.age=input(f"Enter age of {self.name}: ")
    def setMarks(self):
        self.marks=input(f"Enter marks of {self.name}: ")
name1=input("enter your name: ")
roll_no1=input("enter your roll no: ")
s1=Student(name1,roll_no1)
s1.setAge()
s1.setMarks()
s1.display()