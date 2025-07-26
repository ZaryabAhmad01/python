class employee:   
    language="py"
    salary=1200000

    def get_info(self):
        print(f"the language is {self.language} and salary is {self.salary}")
    
    @staticmethod #static method
    def greet():
        print("good morning")

zaryab=employee() 
zaryab.language="js" 
# zaryab.get_info()
employee.get_info(zaryab)
zaryab.greet()