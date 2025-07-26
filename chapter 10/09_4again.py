class Employee:
    language = "py"
    salary = 5000

    def __init__(self,name,salary,language): #dunder method
        self.name=name 
        self.salary=salary
        self.language=language      
        print("hello world")
       

    def getinfo(self):
        print(f"the salary is {self.salary} and the language is {self.language}")
    @staticmethod
    def greet():
        print("good mornig")

zaryab=Employee("zaryab ahmad", 6000,"js")
#zaryab.name="zaryab ahmad"
print(zaryab.name,zaryab.salary,zaryab.language)

#ansari=Empleyee()


