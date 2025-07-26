class employee:   
    language="py"
    salary=1200000   
     
    def __init__(self,name,salary,language):# dundur method which is automaticaly called 
        self.name=name
        self.salary=salary
        self.language=language
        print("i am created an object")


    def get_info(self):# is method ko chalanay ka liye call karni paray gi zaryab.get_info() or employee.get_info(zaryab)
        print(f"the language is {self.language} and salary is {self.salary}")
    
    @staticmethod #static method
    def greet():
        print("good morning")

zaryab=employee("zaryab",13000,"javascript") 
# zaryab.name="zaryab ahmad"
print(zaryab.name,zaryab.salary,zaryab.language) 

# zain=employee()
