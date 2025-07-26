'''🟠 Question 2: Constructor in Inheritance
Create a class Person with a constructor that initializes name and age.
Create a derived class Student that adds a student_id attribute and prints all details using a display() method.
Use super() to call the base class constructor.'''
class person:
    def __init__(self,name,age):# parent class
        self.name=name
        self.age=age
    def super(self):
            print(f"the name is {self.name} and age of person is {self.age}")

class student(person):
    student_id=12
    def display(self):
        print(f"student id is {self.student_id} and name is :{self.name} and age is {self.age}")

a=person("zaryab" , 21)
a.super()
b=student("ansari", 22)
b.super()
b.display()