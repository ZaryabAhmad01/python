class employee:
    company = "itc"

    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

    
class programmer(employee):
    company="tech itc"
    def showlang(self):
        print(f"the name is {self.name} and good in {self.language} language")

a=employee()
b=programmer()
print(a.company,b.company)