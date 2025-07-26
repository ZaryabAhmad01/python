'''💻 Practice Question:
Create a class hierarchy using multiple inheritance.

You are to design a system for an employee management system with the following specifications:

Class Person has attributes: name, age, and a method display().

Class Employee inherits from Person, adds employee_id, and overrides display() to include ID.

Class Department has attribute department_name and a method display().

Class Manager inherits from both Employee and Department, and overrides display() to show all details: name, age, ID, and department.

🧩 Task:
Create the classes as described.

Create an object of class Manager and call the display() method.
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"your name is {self.name} and age is :{self.age}")

class enployee:
    id=12
    def id(self)

